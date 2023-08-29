from typing import List, Optional, Tuple
from .dto import MovieDTO
from .exceptions import MovieExternalServerBugError, ExternalAPIServerError
from .interfaces import MovieServiceInterface
from .repositories import APIMovieRepository


class MovieService(MovieServiceInterface):
    """Service layer to work with movies domain logic"""
    TRIES = 5

    def __init__(self, movie_repository: APIMovieRepository):
        self.movie_repository = movie_repository

    def get_movies(self, skip: int = 0, limit: int = 10, query: Optional[str] = None) -> Tuple[List[MovieDTO], int]:
        """Get movies for query"""

        for _ in range(self.TRIES):
            try:
                movie_dto, total = self.movie_repository.get_movies(skip, limit, query)
                return movie_dto, total
            except MovieExternalServerBugError:
                continue

        raise ExternalAPIServerError(self.TRIES)
