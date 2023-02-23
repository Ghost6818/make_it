from make_it.repositories import UserRepository
import pytest


@pytest.fixture
def repository() -> UserRepository:
    return UserRepository()


def test_can_instantiate_user_repository(
    repository: UserRepository, ) -> None:
    UserRepository()


def test_user_repository_has_add_method(repository: UserRepository):
    with pytest.raises(NotImplementedError):
        repository.add()
