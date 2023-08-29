from rest_framework.exceptions import ValidationError, NotFound


class InvalidOffsetOrLimitError(ValidationError):
    def __init__(self, *args, **kwargs):
        message = "Invalid offset or limit value"
        super().__init__(message, *args, **kwargs)


class PageOutOfRangeError(ValidationError):
    def __init__(self, max_pages, *args, **kwargs):
        message = f"Page out of range. Your query has to be fewer than {max_pages} pages."
        super().__init__(message, *args, **kwargs)


class MovieNotFoundError(NotFound):
    def __init__(self, *args, **kwargs):
        message = "We couldn't find a movie matching your query"
        super().__init__(message, *args, **kwargs)


class MovieExternalServerBugError(RuntimeError):
    def __init__(self, *args):
        message = f"Bug error from movie external server: {args[0]}"
        super().__init__(message, *args)


class ExternalAPIServerError(RuntimeError):
    def __init__(self, *args):
        message = f"External movies services doesn't response in {args[0]} tries"
        super().__init__(message, *args)
