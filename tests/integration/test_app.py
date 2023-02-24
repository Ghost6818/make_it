from make_it.app import app

UNIMPLEMENTED = 501

#test integracyjne sprawdzamy całą aplikacje czy dobrze porejestrowała


def test_get_resource_returns_501_response() -> None:
    result = app.test_client().get('/users')
    assert result.status_code == UNIMPLEMENTED


def test_create_resource_user() -> None:
    payload = {'first_name': 'Nati', 'last_name': 'Nowak'}
    result = app.test_client().post('/users', json=payload)
    assert result.status_code == 201


def test_app_user_create_endpoint() -> None:
    payload = {'first_name': 'Nati', 'last_name': 'Nowak'}
    client = app.test_client()
    response = client.post(path='/users', json=payload)
    assert response.status_code == 201


def test_delete_resource_returns_204_response() -> None:
    result = app.test_client().delete('/users/1')
    assert result.status_code == 204


def test_put_resource_returns_200_response() -> None:
    payload = {'first_name': 'Nati', 'last_name': 'Nowak'}
    result = app.test_client().put('/users/1', json=payload)
    assert result.status_code == 200


def test_patch_resource_returns_200_response() -> None:
    payload = {'first_name': 'Nati'}
    result = app.test_client().patch('/users/1', json=payload)
    assert result.status_code == 200
