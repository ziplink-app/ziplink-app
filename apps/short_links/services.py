import datetime
import json

from apps.common.exceptions import IllegalArgumentException, NotFoundException
from apps.common.models.short_url import ShortUrl
from apps.short_links.helpers import generate_hash


def redirect_url(event: dict) -> str:
    # Convert event to request
    path = event.get("pathParameters", {}).get("param")
    if not path:
        raise IllegalArgumentException(message="Path parameter 'param' is missing.")

    # Query the database for the short URL
    short_url_entry = ShortUrl().get(path)
    if not short_url_entry:
        raise NotFoundException(message="Could not find URL for the given path.")

    # Get the URL from the database
    short_url = short_url_entry.url

    # Ensure it's an absolute URL
    if not short_url.startswith("http://") and not short_url.startswith("https://"):
        raise ValueError(f"Invalid URL in database: {short_url}. Must be absolute.")

    return short_url


def create_redirect_url(event: dict) -> dict:
    url = json.loads(event.get("body", "{}")).get("url")
    if not url:
        raise IllegalArgumentException(message="url is a required field")
    return ShortUrl().create(
        **{
            "url": url,
            "hash": generate_hash(),
            "expires_at": datetime.datetime.now() + datetime.timedelta(hours=1),
        }
    ).to_json()



# @asyncio
# def _update_request_count():
#     pass
