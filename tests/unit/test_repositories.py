from make_it.repositories import UserRepository
import pytest


@pytest.fixture
def repository() -> UserRepository:
    return UserRepository()
class TestUserRepository:
    def test_can_instantiate_user_repository(self):
        repository = UserRepository()
        assert isinstance(repository, UserRepository)

    def test_user_repository_has_add_method(self):
        repository = UserRepository()
        with pytest.raises(NotImplementedError):
            repository.add({})

    def test_user_repository_has_get_method(self):
        repository = UserRepository()
        with pytest.raises(NotImplementedError):
            repository.get(1)

    def test_user_repository_has_update_method(self):
        repository = UserRepository()
        with pytest.raises(NotImplementedError):
            repository.update(1, {})

    def test_user_repository_has_delete_method(self):
        repository = UserRepository()
        with pytest.raises(NotImplementedError):
            repository.delete(1)
