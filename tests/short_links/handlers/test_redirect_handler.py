from apps.short_links.handlers.redirect_handlers import handler
from tests.short_links.handlers.conftest import build_api_gateway_event


def test_api_gateway_event_redirects(set_env_vars, short_url):
    # Given
    event = build_api_gateway_event(short_url.hash)
    # When
    response = handler(event, None)
    # Then
    assert response.get("status_code") == 301
    assert response.get("headers").get("Location") == short_url.url


def test_api_gateway_event__with_invalid_short_url_fails(set_env_vars, short_url):
    # Given
    event = build_api_gateway_event("aklsns")
    # When
    response = handler(event, None)
    # Then
    assert response.get("status_code") == 404
