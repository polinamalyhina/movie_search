from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegistrationAPIView, EmailVerificationAPIView, LoginAPIView, LogoutAPIView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='user_registration'),
    path('verify-email/<uidb64>/<token>/', EmailVerificationAPIView.as_view(), name='user_verification'),
    path('login/', LoginAPIView.as_view(), name='user_login'),
    path('logout/', LogoutAPIView.as_view(), name='user_logout'),
    path('jwt/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
