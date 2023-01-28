import json

import pytest
from flask import request

from make_it.controllers import AddUserController, AddUserRequest, UpdateUserRequest, UpdateUserController


@pytest.fixture
def payload() -> dict:
    return {"firt_name": "Nati", "last_name": "Nowak"}


def test_add_user_controller_has_add_method(capsys, payload: dict) -> None:
    controller = AddUserController()
    request = AddUserRequest(user=payload)
    controller.add(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert  actual == expected


def test_add_user_request_has_user_attribute(payload: dict) -> None:
    requests = AddUserRequest(user=payload)
    assert requests.user


def test_update_user_controller_has_add_method(capsys, payload: dict) -> None:
    controller = UpdateUserController()
    request = UpdateUserRequest(user=payload)
    controller.update(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected


def test_update_user_request_has_user_attribute(payload: dict) -> None:
    requests = UpdateUserRequest(user=payload)
    assert requests.user
