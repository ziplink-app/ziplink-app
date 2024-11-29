from dataclasses import dataclass
from http import HTTPStatus


@dataclass
class ApiException(Exception):
    status_code: int
    message: str


class IllegalArgumentException(ApiException):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message: str):
        super().__init__(status_code=self.status_code, message=message)


class NotFoundException(ApiException):
    status_code = HTTPStatus.NOT_FOUND

    def __init__(self, message: str):
        super().__init__(status_code=self.status_code, message=message)
