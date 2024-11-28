from apps.common.models.short_url import ShortUrl


def redirect_url(event: dict) -> str:
    # Convert event to request
    path = event.get("rawPath")
    # Check for short url in dynamo db
    short_url = ShortUrl().get(path).url
    # Return the short url
    # _update_request_count()
    return short_url


# @asyncio
# def _update_request_count():
#     pass
