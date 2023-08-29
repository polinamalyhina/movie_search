from drf_yasg import openapi


movie_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_INTEGER),
        "title": openapi.Schema(type=openapi.TYPE_STRING),
    },
)

movies_response_data_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "total": openapi.Schema(type=openapi.TYPE_INTEGER),
        "items": openapi.Schema(type=openapi.TYPE_ARRAY, items=movie_schema),
        "page_info": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "current_page": openapi.Schema(type=openapi.TYPE_INTEGER),
                "total_pages": openapi.Schema(type=openapi.TYPE_INTEGER),
                "previous": openapi.Schema(type=openapi.TYPE_STRING),
                "next": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
    },
)

register_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "email": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL, description="User email"),
        "username": openapi.Schema(type=openapi.TYPE_STRING, description="Username"),
    },
    required=["email", "username"],
)

activation_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "message": openapi.Schema(type=openapi.TYPE_STRING, description="Message about email verification"),
        "refresh": openapi.Schema(type=openapi.TYPE_STRING, description="Refresh token"),
        "access": openapi.Schema(type=openapi.TYPE_STRING, description="Access token"),
    },
    required=["email", "password"],
)

login_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "refresh": openapi.Schema(type=openapi.TYPE_STRING, description="The JWT refresh token"),
        "access": openapi.Schema(type=openapi.TYPE_STRING, description="The JWT access token"),
    },
    required=["refresh", "access"]
)

logout_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "message": openapi.Schema(type=openapi.TYPE_STRING, description="Message about logout"),
    },
    required=["refresh", "access"]
)
