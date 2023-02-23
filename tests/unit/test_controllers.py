import json
from unittest.mock import Mock

import pytest
from _pytest.capture import CaptureFixture

from make_it.controllers import AddUserController, AddUserRequest, UpdateUserRequest, UpdateUserController
from make_it.repositories import UserRepository


@pytest.fixture
def payload() -> dict:
    return {"firt_name": "Nati", "last_name": "Nowak"}


@pytest.fixture
def user_repository() -> UserRepository:
    return Mock(UserRepository)


@pytest.fixture
def controller(user_repository: UserRepository) -> AddUserController:
    return AddUserController(repository=user_repository)


def test_add_user_controller_has_add_method(
    controller: AddUserController,
    capsys: CaptureFixture,
    payload: dict) -> None:
    request = AddUserRequest(user=payload)
    controller.add(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected


def test_calls_add_in_repository_on_calling_controller(
    controller: AddUserController,
    repository: UserRepository,
    payload: dict,) -> None:
    request = AddUserRequest(user=payload)
    controller.add(request)
    assert repository.add.call_count > 0


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
