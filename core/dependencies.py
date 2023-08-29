from movies.repositories import APIMovieRepository
from movies.services import MovieService


class DependencyContainer:
    def get_movie_service(self) -> MovieService:
        repository = APIMovieRepository()
        return MovieService(repository)
