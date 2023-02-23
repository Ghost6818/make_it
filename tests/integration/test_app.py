from make_it.app import app

UNIMPLEMENTED = 501

#test integracyjne sprawdzamy całą aplikacje czy dobrze porejestrowała


def test_get_resource_returns_501_response() -> None:
    result = app.test_client().get('/api/resource')
    assert result.status_code == UNIMPLEMENTED


def test_create_resource_user() -> None:
    result = app.create_user()
    assert result.status_code == UNIMPLEMENTED


def test_app_user_create_endpoint() -> None:
    payload = {'first_name': 'Nati', 'last_name': 'Nowak'}
    client = app.test_client()
    response = client.post(path='/users', json=payload)
    assert response.status_code == 200


def test_post_resource_returns_501_response() -> None:
    result = app.test_client().post('/api/resource')
    assert result.status_code == UNIMPLEMENTED


def test_delete_resource_returns_501_response() -> None:
    result = app.test_client().delete('/api/resource/1')
    assert result.status_code == UNIMPLEMENTED


def test_put_resource_returns_501_response() -> None:
    result = app.test_client().put('/api/resource/2')
    assert result.status_code == UNIMPLEMENTED


def test_patch_resource_returns_501_response() -> None:
    result = app.test_client().patch('/api/resource/3')
    assert result.status_code == UNIMPLEMENTED
