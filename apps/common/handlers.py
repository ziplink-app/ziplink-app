from functools import wraps
from http import HTTPStatus
from typing import Callable

from apps.common.exceptions import ApiException
from apps.common.logging import get_logger

logger = get_logger(__name__)

def handler(func: Callable[[dict, dict], dict]) -> Callable[[dict, dict], dict]:
    @wraps(func)
    def wrapper(event: dict, context: dict) -> dict:
        try:
            # todo enable logging
            return func(event, context)
        except ApiException as apie:
            logger.error(f"Api Error: {str(apie)}")
            return {"statusCode": apie.status_code, "message": apie.message}
        except Exception as e:
            # Handle unexpected exceptions
            logger.error(f"Internal Server Error: {str(e)}")
            return {"statusCode": HTTPStatus.INTERNAL_SERVER_ERROR, "message": f"Internal Server Error: {str(e)}"}

    return wrapper
