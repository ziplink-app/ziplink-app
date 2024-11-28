from apps.short_links.services.redirect_services import redirect_url


def handler(event: dict, context: dict):
    short_url = redirect_url(event)
    if short_url:
        return {"status_code": 301, "headers": {"Location": short_url}}
    else:
        return {"status_code": 404}
