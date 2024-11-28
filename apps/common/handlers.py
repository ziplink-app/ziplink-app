from functools import wraps
from http import HTTPStatus
from typing import Callable

from apps.common.exceptions import ApiException


def handler(func: Callable[[dict, dict], dict]) -> Callable[[dict, dict], dict]:
    @wraps(func)
    def wrapper(event: dict, context: dict) -> dict:
        try:
            # todo enable logging
            return func(event, context)
        except ApiException as apie:
            return {"status_code": apie.status_code, "message": apie.message}
        except Exception as e:
            # Handle unexpected exceptions
            return {"status_code": HTTPStatus.INTERNAL_SERVER_ERROR, "message": f"Internal Server Error: {str(e)}"}

    return wrapper
