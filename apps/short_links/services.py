import datetime

from apps.common.exceptions import IllegalArgumentException, NotFoundException
from apps.common.models.short_url import ShortUrl
from apps.short_links.helpers import generate_hash


def redirect_url(event: dict) -> str:
    # Convert event to request
    path = event.get("rawPath")
    # Check for short url in dynamo db
    short_url = ShortUrl().get(path).url
    if not short_url:
        raise NotFoundException(message="Could not find url")
    # Return the short url
    # _update_request_count()
    return short_url


def create_redirect_url(event: dict) -> dict:
    url = event.get("body", {}).get("url")
    if not url:
        raise IllegalArgumentException(message="url is a required field")
    return ShortUrl().create(
        **{
            "url": url,
            "hash": generate_hash(),
            "ttl": datetime.datetime.now(),
        }
    ).to_json()



# @asyncio
# def _update_request_count():
#     pass
