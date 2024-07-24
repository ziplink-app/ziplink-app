from apps.redirect.services import redirect_url


def handler(event: dict, context: dict):
    short_url = redirect_url(event)
    return {"status_code": 301, "headers": {"Location": short_url}}
