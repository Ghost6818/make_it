from unittest.mock import Mock

import pytest
from flask import Response
from flask.views import MethodView

from make_it.controllers import (
    GetUserController, AddUserController, PutUserController,
    PatchUserController, DeleteUserController
)
from make_it.views import (
    DeleteUserView, GetUserView, PostUserView,
    PatchUserView, PutUserView
)


@pytest.fixture
def get_user_controller() -> Mock:
    return Mock(GetUserController)


@pytest.fixture
def add_user_controller() -> Mock:
    return Mock(AddUserController)


@pytest.fixture
def put_user_controller() -> Mock:
    return Mock(PutUserController)


@pytest.fixture
def patch_user_controller() -> Mock:
    return Mock(PatchUserController)


@pytest.fixture
def delete_user_controller() -> Mock:
    return Mock(DeleteUserController)


@pytest.fixture
def get_user_view(get_user_controller: GetUserController) -> GetUserView:
    return GetUserView(controller=get_user_controller)


@pytest.fixture
def post_user_view(add_user_controller: AddUserController) -> PostUserView:
    return PostUserView(controller=add_user_controller)


@pytest.fixture
def put_user_view(put_user_controller: PutUserController) -> PutUserView:
    return PutUserView(controller=put_user_controller)


@pytest.fixture
def patch_user_view(patch_user_controller: PatchUserController) -> PatchUserView:
    return PatchUserView(controller=patch_user_controller)


@pytest.fixture
def delete_user_view(delete_user_controller: DeleteUserController) -> DeleteUserView:
    return DeleteUserView(controller=delete_user_controller)


def test_get_user_view_returns_501_on_get_method(get_user_view: GetUserView) -> None:
    actual = get_user_view.get("1")
    assert actual.status_code == 501


def test_get_user_view_response_on_get_method(get_user_view: GetUserView) -> None:
    actual = get_user_view.get("2")
    assert isinstance(actual, Response)


def test_get_user_view_is_subclass_of_method_view(get_user_view: GetUserView) -> None:
    assert isinstance(get_user_view, MethodView)


def test_get_user_controller_is_called_on_get_method(get_user_view: GetUserView, get_user_controller: Mock) -> None:
    get_user_view.get("1")
    assert get_user_controller.get.call_count > 0


def test_post_user_view_is_subclass_of_method_view(post_user_view: PostUserView) -> None:
    assert isinstance(post_user_view, MethodView)


def test_put_user_view_is_subclass_of_method_view(put_user_view: PutUserView) -> None:
    assert isinstance(put_user_view, MethodView)


def test_patch_user_view_is_subclass_of_method_view(patch_user_view: PatchUserView) -> None:
    assert isinstance(patch_user_view, MethodView)


def test_delete_user_view_is_subclass_of_method_view(delete_user_view: DeleteUserView) -> None:
    assert isinstance(delete_user_view, MethodView)