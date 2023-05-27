from typing import Tuple

from flask import Flask, Response, request, jsonify
import json
from make_it.controllers import DeleteUserController, GetUserController, \
    AddUserRequest, AddUserController, PatchUserController, PutUserController
from make_it.repositories import UserRepository
from make_it.views import DeleteUserView, GetUserView, PostUserView, PatchUserView, PutUserView

app = Flask(__name__)


@app.get("/ping")
def ping():
    return Response(status=501)


get_user_view = GetUserView.as_view("user_view", controller=GetUserController())
post_user_view = PostUserView.as_view("post_user_view", controller=AddUserController())
put_user_view = PutUserView.as_view("put_user_view", controller=PutUserController())
patch_user_view = PatchUserView.as_view("patch_user_view", controller=PatchUserController())
delete_user_view = DeleteUserView.as_view("delete_user_view", controller=DeleteUserController())

app.add_url_rule("/users/<id>", view_func=get_user_view, methods=["GET"])
app.add_url_rule("/users", view_func=post_user_view, methods=["POST"])
app.add_url_rule("/users/<id>", view_func=put_user_view, methods=["PUT"])
app.add_url_rule("/users/<id>", view_func=patch_user_view, methods=["PATCH"])
app.add_url_rule("/users/<id>", view_func=delete_user_view, methods=["DELETE"])



#na lekcji
# @app.get('/users/<id>')
# def get_user(id) -> Response:
#     controller = GetUserController()
#     try:
#         controller.get(request=id)
#     except NotImplementedError:
#         pass
#     return Response(status=501)

# @app.post('/users')
# def create_user() -> tuple[Response, int]:
#     user = request.json
#     repository = UserRepository()
#     controller = AddUserController(repository=repository)
#     add_user_request = AddUserRequest(user=user)
#     controller.add(request=add_user_request)
#     return jsonify(user), 201


# @app.route('/users/<user_id>', methods=['PATCH'])
# def patch_user(user_id):
#     user = request.json
#     key = next(iter(user)) # get the first (and only) key in the dictionary
#     return jsonify({key: user[key]}), 200


# @app.delete('/users/<user_id>')
# def delete_user(user_id) -> Response:
#     try:
#         controller = DeleteUserController()
#         controller.delete(request=user_id)
#     except NotImplementedError:
#         pass
#     return Response(status=204)


# @app.route('/users/<user_id>', methods=['PUT'])
# def update_user() -> Response:
#     user = request.json
#     try:
#         controller = UpdateUserController()
#         update_user_request = UpdateUserRequest(user=user)
#         controller.update(request=update_user_request)
#     except NotImplementedError:
#         pass
#     return jsonify(user)
