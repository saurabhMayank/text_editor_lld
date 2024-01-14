
class BaseExceptionError(Exception):
    """
    Base Exception class for v2 APIs.
    All custom exceptions are created by extending this class.
    Exception has 4 attributes corresponding to details sent in 'error' object
    in response JSON -
        status - http status code
        code - application specific error code
        title - title of error
        detail - details of error
    """

    def __init__(self, status, code, title, detail):
        Exception.__init__(self)
        self.title = title
        self.detail = detail

    def as_dict(self):
        return {"title": self.title, "detail": self.detail}

    def as_str(self):
        exception_str = "Exception Type : " + self.__class__.__name__
        exception_str += "\nTitle - " + self.title if self.title else ""
        exception_str += "\nDetails - " + self.detail if self.detail else ""
        return exception_str

    def __str__(self):
        return f"{self.__class__.__name__} ({self.title}): {self.detail}"


class SizeOutofBoundsError(BaseExceptionError):
    def __init__(self, title=None, detail=None):
        self.title = "Size out of Bounds"
        if detail:
            self.detail = detail

class TextNotFoundError(BaseExceptionError):
    def __init__(self, title=None, detail=None):
        self.title = "Text Not Found"
        if detail:
            self.detail = detail

class NoTextCopiedError(BaseExceptionError):
    def __init__(self, title=None, detail=None):
        self.title = "No Text Copied"
        if detail:
            self.detail = detail