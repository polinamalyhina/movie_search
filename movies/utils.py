from typing import Tuple
from rest_framework.request import Request


class NavigationHelper:
    def __init__(self, total: int, limit: int, offset: int, request: Request, query: str | None):
        self.total = total
        self.limit = limit
        self.offset = offset
        self.request = request
        self.query = query

    def calculate_current_and_total_pages(self) -> Tuple[bool, bool, int, int]:
        current_page = (self.offset // self.limit) + 1
        total_pages = (self.total // self.limit) + 1 if self.total % self.limit != 0 else self.total // self.limit
        has_previous = current_page > 1
        has_next = current_page < total_pages
        return has_previous, has_next, current_page, total_pages

    def calculate_prev_and_next_offsets(self) -> Tuple[int, int]:
        next_offset = self.offset + self.limit
        prev_offset = max(self.offset - self.limit, 0)
        return prev_offset, next_offset

    def generate_navigation_links(self, prev_offset: int, next_offset: int):
        base_url = f"{self.request.scheme}://{self.request.get_host()}{self.request.path}"
        if self.query:
            prev_page_url = f"{base_url}?offset={prev_offset}&limit={self.limit}&query={self.query}"
            next_page_url = f"{base_url}?offset={next_offset}&limit={self.limit}&query={self.query}"
        else:
            prev_page_url = f"{base_url}?offset={prev_offset}&limit={self.limit}"
            next_page_url = f"{base_url}?offset={next_offset}&limit={self.limit}"
        return prev_page_url, next_page_url
