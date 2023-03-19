from dataclasses import dataclass
from make_it.domain import GetUsersRequest, PutUserRequest, PatchUserRequest, DeleteUserRequest


@dataclass
class AddUserRequest:
    user: dict


class AddUserController:
    def add(self, request: AddUserRequest) -> None:
        print(request.user)


@dataclass
class UpdateUserRequest:
    user: dict


class UpdateUserController:
    def update(self, request: UpdateUserRequest) -> None:
        print(request.user)


class GetUsersController:
    def get(self, request: GetUsersRequest) -> dict:
        raise NotImplementedError()


class PutUserController:
    def put(self, request: PutUserRequest) -> dict:
        raise NotImplementedError()


class PatchUserController:
    def patch(self, request: PatchUserRequest) -> dict:
        raise NotImplementedError()


class DeleteUserController:
    def delete(self, request: DeleteUserRequest) -> None:
        raise NotImplementedError()


class GetUserController:
    def get(self, request) -> None:
        raise NotImplementedError()
