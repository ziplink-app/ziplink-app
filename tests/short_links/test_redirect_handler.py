from http import HTTPStatus

from apps.short_links.handlers import redirect_handler
from tests.short_links.conftest import build_api_gateway_event
from tests.conftest import set_env_vars

def test_api_gateway_event_redirects(set_env_vars, short_url):
    # Given
    event = build_api_gateway_event("GET", short_url.hash)
    # When
    response = redirect_handler(event, None)
    # Then
    assert response.get("status_code") == HTTPStatus.MOVED_PERMANENTLY
    assert response.get("headers").get("Location") == short_url.url


def test_api_gateway_event__with_invalid_short_url_fails(set_env_vars, short_url):
    # Given
    event = build_api_gateway_event("GET", "aklsns")
    # When
    response = redirect_handler(event, None)
    # Then
    assert response.get("status_code") == HTTPStatus.NOT_FOUND
