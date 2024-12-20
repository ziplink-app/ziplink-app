from apps.common.handlers import handler
from apps.common.logging import get_logger
from apps.short_links.services import create_redirect_url, redirect_url

logger = get_logger(__name__)

@handler
def redirect_handler(event: dict, context: dict):
    logger.info(event)
    short_url = redirect_url(event)
    if short_url:
        return {"statusCode": 301, "headers": {"Location": short_url}}
    else:
        return {"statusCode": 404}

@handler
def create_handler(event: dict, context: dict):
    response = create_redirect_url(event)
    if response:
        return {"statusCode": 201, "body": response}
    else:
        return {"statusCode": 404}
