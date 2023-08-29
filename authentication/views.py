from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login, logout
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status, exceptions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from core.schemas import register_request_schema, register_response_schema, \
    activation_response_schema, login_response_schema, login_request_schema, logout_response_schema
from .exceptions import EmailSendingError, AlreadyVerifiedError, InvalidTokenError, InvalidEmailOrPasswordError, \
    DoesNotActiveError, DoesNotExistError
from .models import CustomUser
from .serializers import RegistrationDTOSerializer, LoginDTOSerializer, CustomTokenObtainPairSerializer
from .tasks import Notifications


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegistrationAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_description="Register a new user with profile",
        request_body=RegistrationDTOSerializer,
        responses={
            201: register_response_schema,
            400: 'Bad Request',
        },
        tags=["auth"],
        security=[],
    )
    def post(self, request):
        serializer = RegistrationDTOSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save(password=make_password(serializer.validated_data['password']))

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        verification_link = f"{request.scheme}://{request.get_host()}/api/v1/authentication/verify-email/{uid}/{token}/"
        message = f"Please verify your email address by clicking the link below:\n\n{verification_link}"
        notification = Notifications
        try:
            notification.send_email_async.delay(
                "Verify your email address",
                message,
                "noreply@example.com",
                [user.email],
                fail_silently=False,
            )
        except Exception as e:
            print(str(e))
            raise EmailSendingError()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmailVerificationAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_description="Activate user via email",
        responses={
            201: activation_response_schema,
            400: 'Bad Request',
        },
        tags=["auth"],
        security=[],
    )
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_object_or_404(CustomUser, pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            raise EmailSendingError()

        if not default_token_generator.check_token(user, token):
            raise InvalidTokenError()

        if user.is_active:
            raise AlreadyVerifiedError()

        refresh = RefreshToken.for_user(user)
        user.is_active = True
        user.save()

        return Response(
            {"message": "Email verified successfully", "refresh": str(refresh), "access": str(refresh.access_token)},
            status=status.HTTP_200_OK,
        )


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_description="Login",
        request_body=LoginDTOSerializer,
        responses={
            201: login_response_schema,
            400: 'Bad Request',
        },
        tags=["auth"],
        security=[],
    )
    def post(self, request):
        serializer = LoginDTOSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = CustomUser.objects.get(email=email)
            if user is not None:
                if user.is_active:
                    if user.check_password(password):
                        login(request, user)
                        refresh = RefreshToken.for_user(user)
                        return Response({"refresh": str(refresh), "access": str(refresh.access_token)},
                                        status=status.HTTP_200_OK)
                    else:
                        raise InvalidEmailOrPasswordError()
                else:
                    raise DoesNotActiveError()
            else:
                raise DoesNotExistError()
        except exceptions.ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Logout",
        responses={
            201: logout_response_schema,
            400: 'Bad Request',
        },
        tags=["auth"],
        security=[],
    )
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully."})
