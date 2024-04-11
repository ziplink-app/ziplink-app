import asyncio

from src.repository.short_url_repository import ShortUrlRepository


def redirect_url(event: dict) -> str:
    # Convert event to request
    path = event.get("rawPath")
    # Check for short url in dynamo db
    short_url = ShortUrlRepository().get_short_url(path)
    # Return the short url
    _update_request_count()
    return short_url


@asyncio
def _update_request_count():
    pass
