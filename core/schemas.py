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
