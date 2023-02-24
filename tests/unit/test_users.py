import json

import pytest
from make_it.app import app


@pytest.fixture
def payload() -> dict:
    return {"name": "Nati", "email": "nati@example.com"}


def test_ping_endpoint() -> None:
    with app.test_client() as client:
        response = client.get('/ping')
        assert response.status_code == 501


def test_get_users_endpoint() -> None:
    with app.test_client() as client:
        response = client.get('/users')
        assert response.status_code == 501


def test_create_user_endpoint(payload: dict) -> None:
    with app.test_client() as client:
        response = client.post('/users', json=payload)
        assert response.status_code == 201
        assert response.get_json() == payload


def test_update_user_endpoint(payload: dict) -> None:
    with app.test_client() as client:
        response = client.put('/users/1', json=payload)
        assert response.status_code == 200
        assert response.get_json() == payload


def test_patch_user_endpoint(payload: dict) -> None:
    with app.test_client() as client:
        response = client.patch('/users/1', json=payload)
        assert response.status_code == 200
        key = next(iter(payload))
        assert response.get_json() == {key: payload[key]}


def test_delete_user_endpoint() -> None:
    with app.test_client() as client:
        response = client.delete('/users/1')
        assert response.status_code == 204