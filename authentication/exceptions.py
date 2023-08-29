from rest_framework import status
from rest_framework.exceptions import APIException


class EmailSendingError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, *args, **kwargs):
        message = "An error occurred while sending the verification email"
        super().__init__(message, *args, **kwargs)


class AlreadyVerifiedError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, *args, **kwargs):
        message = "Email already verified"
        super().__init__(message, *args, **kwargs)


class InvalidTokenError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, *args, **kwargs):
        message = "Invalid token"
        super().__init__(message, *args, **kwargs)


class InvalidEmailOrPasswordError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED

    def __init__(self, *args, **kwargs):
        message = "Invalid email or password"
        super().__init__(message, *args, **kwargs)


class DoesNotActiveError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED

    def __init__(self, *args, **kwargs):
        message = "User account is not active"
        super().__init__(message, *args, **kwargs)


class DoesNotExistError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED

    def __init__(self, *args, **kwargs):
        message = "User does not exist"
        super().__init__(message, *args, **kwargs)
