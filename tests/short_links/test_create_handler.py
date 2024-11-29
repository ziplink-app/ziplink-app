import json
from http import HTTPStatus

from apps.short_links.handlers import create_handler
from tests.short_links.conftest import build_api_gateway_event
from tests.conftest import set_env_vars

def test_api_gateway_event_creates_new_redirect_url(set_env_vars, short_url):
    # Given
    url = {"url": "www.google.com"}
    event = build_api_gateway_event("POST", "", url)
    # When
    response = create_handler(event, None)
    response_json = json.loads(response.get("body"))
    # Then
    assert response.get("status_code") == HTTPStatus.CREATED
    assert response_json.get("url") == url.get("url")


def test_api_gateway_event_does_not_creates_new_redirect_url_for_no_url(set_env_vars, short_url):
    # Given
    url = {"nothing": ""}
    event = build_api_gateway_event("POST", "", url)
    # When
    response = create_handler(event, None)
    # Then
    assert response.get("status_code") == HTTPStatus.BAD_REQUEST


def test_api_gateway_event_doesn_not_creates_new_redirect_url_for_blank_url(set_env_vars, short_url):
    # Given
    url = {"url": ""}
    event = build_api_gateway_event("POST", "", url)
    # When
    response = create_handler(event, None)
    # Then
    assert response.get("status_code") == HTTPStatus.BAD_REQUEST