from make_it.app import ping, get_resource, create_resource, delete_resource, update_resource, patch_resource

UNIMPLEMENTED = 501


def test_ping_returns_501_response() -> None:
    result = ping()
    assert result.status_code == UNIMPLEMENTED


def test_get_resource_returns_501_response() -> None:
    result = get_resource()
    assert result.status_code == UNIMPLEMENTED


def test_post_resource_returns_501_response() -> None:
    result = create_resource()
    assert result.status_code == UNIMPLEMENTED


def test_delete_resource_returns_501_response() -> None:
    resource_id = "1"
    result = delete_resource(resource_id)
    assert result.status_code == UNIMPLEMENTED


def test_put_resource_returns_501_response() -> None:
    resource_id = "2"
    result = update_resource(resource_id)
    assert result.status_code == UNIMPLEMENTED


def test_patch_resource_returns_501_response() -> None:
    resource_id = "3"
    result = patch_resource(resource_id)
    assert result.status_code == UNIMPLEMENTED
