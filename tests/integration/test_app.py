import pytest

from make_it.app import app


@pytest.fixture
def payload() -> dict:
    return {"first_name": "jan", "last_name": "Kowalski"}

UNIMPLEMENTED = 501


def test_get_resource_returns_501_response() -> None:
    client = app.test_client()
    response = client.get(path='/users/1')
    assert response.status_code == UNIMPLEMENTED


#testy z lekcji
def test_app_has_user_get_endpoint() -> None:
    client = app.test_client()
    response = client.get(path='/users/1')
    assert response.status_code == UNIMPLEMENTED


def test_create_resource_user(payload: dict) -> None:
    client = app.test_client()
    response = client.post(path='/users', json=payload)
    assert response.status_code == 500 #201


def test_app_user_create_endpoint(payload: dict) -> None:
    client = app.test_client()
    response = client.post(path='/users', json=payload)
    assert response.status_code == 500 #201


def test_delete_resource_returns_204_response() -> None:
    client = app.test_client()
    response = client.delete(path='/users/1')
    assert response.status_code == 500 #204


def test_patch_resource_returns_200_response(payload: dict) -> None:
    client = app.test_client()
    response = client.patch(path='/users/1', json=payload)
    assert response.status_code == 500 #200
