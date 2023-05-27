from flask import Response
from flask.views import MethodView

from make_it.controllers import GetUserController, AddUserController

from flask import Flask, Response, request, jsonify, make_response
from .controllers import AddUserController, AddUserRequest, UpdateUserRequest, GetUserController, GetUserRequest, PutUserController, PutUserRequest, PatchUserController, PatchUserRequest, DeleteUserController, DeleteUserRequest


class GetUserView(MethodView):
    def __init__(self, controller: GetUserController) -> None:
        self._get_user_controller = controller

    def get(self, id: str) -> Response:
        try:
            self._get_user_controller.get(int(id))
        except NotImplementedError:
            pass
        return Response(status=501)


class PostUserView(MethodView):
    def __init__(self, controller: AddUserController) -> None:
        self._post_user_controller = controller

    def post(self) -> Response:
        user = request.json
        try:
            self._post_user_controller.get(request=AddUserRequest(user=user))
        except NotImplementedError:
            pass
        return make_response(jsonify(user), 201)


class PutUserView(MethodView):
    def __init__(self, controller: PutUserController) -> None:
        self._put_user_controller = controller

    def put(self, id: str) -> Response:
        user = request.json
        try:
            self._put_user_controller.get(request=PutUserRequest(user=user), id=int(id))
        except NotImplementedError:
            pass
        return make_response(jsonify(user), 200)


class PatchUserView(MethodView):
    def __init__(self, controller: PatchUserController) -> None:
        self._patch_user_controller = controller

    def patch(self, id: str) -> Response:
        user = request.json
        try:
            self._patch_user_controller.get(request=PatchUserRequest(user=user), id=int(id))
        except NotImplementedError:
            pass
        return make_response(jsonify(user), 200)


class DeleteUserView(MethodView):
    def __init__(self, controller: DeleteUserController) -> None:
        self._delete_user_controller = controller

    def delete(self, id: str) -> Response:
        try:
            self._delete_user_controller.get(id=int(id))
        except NotImplementedError:
            pass
        return Response(status=204)
