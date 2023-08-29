from abc import ABCMeta, abstractmethod
from typing import List
from .dto import MovieDTO


class MovieRepositoryInterface(metaclass=ABCMeta):
    """Interface for MovieRepository"""

    @abstractmethod
    def get_movies(self, page: int, per_page: int, query: str) -> List[MovieDTO]:
        pass


class MovieServiceInterface(metaclass=ABCMeta):
    """Interface for MovieService"""

    @abstractmethod
    def get_movies(self, page: int, per_page: int, query: str) -> List[MovieDTO]:
        pass
