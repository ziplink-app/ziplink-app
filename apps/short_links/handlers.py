from apps.common.handlers import handler
from apps.short_links.services import create_redirect_url, redirect_url


@handler
def redirect_handler(event: dict, context: dict):
    short_url = redirect_url(event)
    if short_url:
        return {"status_code": 301, "headers": {"Location": short_url}}
    else:
        return {"status_code": 404}

@handler
def create_handler(event: dict, context: dict):
    response = create_redirect_url(event)
    if response:
        return {"status_code": 201, "body": response}
    else:
        return {"status_code": 404}
