from dataclasses import dataclass
from typing import Dict
from make_it.domain import AddUserRequest, GetUsersRequest, PutUserRequest, PatchUserRequest, DeleteUserRequest


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
# exeption hendler in app.py

class GetUserController:
    def get(self, request) -> None:
        raise NotImplementedError()

