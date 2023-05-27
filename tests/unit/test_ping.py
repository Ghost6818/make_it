#testy jednostkowe; testy unity sprawdzamy czy funkcja działa poprawnie

from make_it.app import app

UNIMPLEMENTED = 501


def test_get_resource_returns_501_response() -> None:
    with app.test_client() as client:
        result = client.get('/resource')
        assert result.status_code == 404


def test_post_resource_returns_501_response() -> None:
    with app.test_client() as client:
        result = client.post('/resource')
        assert result.status_code == 404


def test_delete_resource_returns_501_response() -> None:
    with app.test_client() as client:
        resource_id = "1"
        result = client.delete(f'/resource/{resource_id}')
        assert result.status_code == 404


def test_put_resource_returns_501_response() -> None:
    with app.test_client() as client:
        resource_id = "2"
        result = client.put(f'/resource/{resource_id}')
        assert result.status_code == 404


def test_patch_resource_returns_501_response() -> None:
    with app.test_client() as client:
        resource_id = "3"
        result = client.patch(f'/resource/{resource_id}')
        assert result.status_code == 404
