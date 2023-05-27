from dataclasses import dataclass
from make_it.domain import GetUsersRequest, PutUserRequest, PatchUserRequest, DeleteUserRequest


@dataclass
class GetUserRequest:
    user_id: int


@dataclass
class AddUserRequest:
    user: dict


@dataclass
class UpdateUserRequest:
    user: dict


@dataclass
class PutUserRequest:
    user: dict


@dataclass
class PatchUserRequest:
    user: dict


@dataclass
class DeleteUserRequest:
    user_id: int



class GetUserController:
    def get(self, id: int):
        raise NotImplementedError


class AddUserController:
    def add(self, request: AddUserRequest):
        raise NotImplementedError


class PutUserController:
    def put(self, request: PutUserRequest, id: int):
        raise NotImplementedError


class PatchUserController:
    def patch(self, request: PatchUserRequest, id: int):
        raise NotImplementedError


class DeleteUserController:
    def delete(self, id: int):
        raise NotImplementedError
