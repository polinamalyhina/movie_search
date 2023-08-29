from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from core.dependencies import DependencyContainer
from core.schemas import movies_response_data_schema
from .exceptions import ExternalAPIServerError, MovieNotFoundError, InvalidOffsetOrLimitError, PageOutOfRangeError
from .serializers import MovieDTOSerializer
from .utils import NavigationHelper


class MoviesView(APIView):
    @swagger_auto_schema(
        operation_description="Get movies",
        responses={
            201: movies_response_data_schema,
            400: 'Bad Request',
        },
        tags=["auth"],
        security=[],
    )
    def get(self, request):
        offset, limit, query = self._get_pagination_args(request)

        container = DependencyContainer()

        movie_service = container.get_movie_service()
        try:
            movies, total = movie_service.get_movies(offset, limit, query)
            if total == 0:
                raise MovieNotFoundError()
        except ExternalAPIServerError as exception:
            Response({"detail": str(exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if offset >= total:
            raise PageOutOfRangeError((total // limit) + 1)

        navigator_paginator = NavigationHelper(total, limit, offset, request, query)

        has_previous, has_next, current_page, total_pages = navigator_paginator.calculate_current_and_total_pages()
        prev_offset, next_offset = navigator_paginator.calculate_prev_and_next_offsets()
        prev_page_url, next_page_url = navigator_paginator.generate_navigation_links(prev_offset, next_offset)

        serializer = MovieDTOSerializer(movies, many=True)
        response_data = {
            "total": total,
            "items": serializer.data,
            "page_info": {
                "current_page": current_page,
                "total_pages": total_pages,
                "previous": prev_page_url if has_previous else None,
                "next": next_page_url if has_next else None,
            }
        }

        return Response(response_data)

    def _get_pagination_args(self, request):
        offset = request.GET.get('offset', 0)
        limit = request.GET.get('limit', 10)
        query = request.GET.get('query', '')

        try:
            offset = int(offset)
            limit = int(limit)
            if offset < 0 or limit <= 0:
                raise InvalidOffsetOrLimitError()
        except ValueError:
            raise InvalidOffsetOrLimitError()

        return offset, limit, query
