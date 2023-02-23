from dataclasses import dataclass
from typing import Dict


@dataclass
class AddUserRequest:
    json: Dict


@dataclass
class GetUsersRequest:
    pass


@dataclass
class PutUserRequest:
    id: int
    json: Dict


@dataclass
class PatchUserRequest:
    id: int
    json: Dict


@dataclass
class DeleteUserRequest:
    id: int
