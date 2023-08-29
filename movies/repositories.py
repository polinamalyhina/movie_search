import os
import requests
from typing import List, Tuple
from .dto import MovieDTO
from .exceptions import MovieExternalServerBugError
from .interfaces import MovieRepositoryInterface


class APIMovieRepository(MovieRepositoryInterface):
    def get_movies(self, offset: int, limit: int, query: str) -> Tuple[List[MovieDTO], int]:

        api_url = os.getenv('BASE_URL', '')
        params = {
            "skip": offset,
            "limit": limit,
            "query": query
        }
        response = requests.get(f"{api_url}/movies/", params=params)
        if str(response.status_code).startswith("40"):
            raise MovieExternalServerBugError(response.status_code)
        data = response.json()
        items = [MovieDTO(id=item["id"], title=item["title"]) for item in data["items"]]
        total = data["total"]
        return items, total
