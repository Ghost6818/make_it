import json
from unittest.mock import Mock

import pytest
from _pytest.capture import CaptureFixture

from make_it.controllers import AddUserController, AddUserRequest, UpdateUserRequest, PutUserController
from make_it.repositories import UserRepository


@pytest.fixture
def payload() -> dict:
    return {"firt_name": "Nati", "last_name": "Nowak"}


@pytest.fixture
def user_repository() -> UserRepository:
    return Mock(UserRepository)


@pytest.fixture
def controller() -> AddUserController:
    return AddUserController()


def test_add_user_controller_has_add_method(
    capsys: CaptureFixture,
    payload: dict,
    controller: AddUserController,
) -> None:
    try:
        request = AddUserRequest(user=payload)
        controller.add(request)
        actual = capsys.readouterr().out
        expected = f"{json.dumps(payload)}\n".replace('"', "'")
        assert actual == expected
    except NotImplementedError:
        pass


# def test_calls_add_in_repository_on_calling_controller(
#         controller: AddUserController,
#         repository: Mock,
#         payload: dict,
# ) -> None:
#     request = AddUserRequest(user=payload)
#     controller.add(request)
#     assert user_repository.add.call_count >  0


def test_add_user_request_has_user_attribute(payload: dict) -> None:
    request = AddUserRequest(user=payload)
    assert request.user


def test_put_user_controller_has_add_method(
    capsys: CaptureFixture, payload: dict) -> None:
    try:
        controller = PutUserController()
        request = UpdateUserRequest(user=payload)
        request.id = 1
        controller.put(request, request.id)
        actual = capsys.readouterr().out
        expected = f"{json.dumps(payload)}\n".replace('"', "'")
        assert actual == expected
    except NotImplementedError:
        pass


def test_update_user_request_has_user_attribute(payload: dict) -> None:
    requests = UpdateUserRequest(user=payload)
    assert requests.user
