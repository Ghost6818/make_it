import json

import pytest
from make_it.app import app
from make_it.app import create_user, update_user


@pytest.fixture
def payload() -> dict:
    return {"firt_name": "Nati", "last_name": "Nowak"}


def test_app_user_create_endpoint(payload: dict) -> None:
    with app.test_request_context(method='POST', json=payload):
        result = create_user()
    assert result.json == payload


def test_app_user_prints_user_on_console(payload: dict, capsys) -> None:
    with app.test_request_context(method='POST', json=payload):
        create_user()
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected


def test_app_user_update_endpoint(payload: dict) -> None:
    with app.test_request_context(method='POST', json=payload):
        result = update_user()
    assert result.json == payload
 