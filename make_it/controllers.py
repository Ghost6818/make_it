from dataclasses import dataclass


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
