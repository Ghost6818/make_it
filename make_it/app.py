from flask import Flask, Response, request, jsonify
import json
from make_it.controllers import UpdateUserController, UpdateUserRequest, DeleteUserController, GetUserController
from make_it.views import UserView

app = Flask(__name__)


@app.get("/ping")
def ping():
    return Response(status=501)


@app.route('/users', methods=['GET'])
def get_resource():
    return Response(status=501)

#na lekcji
# @app.get('/users/<id>')
# def get_user(id) -> Response:
#     controller = GetUserController()
#     try:
#         controller.get(request=id)
#     except NotImplementedError:
#         pass
#     return Response(status=501)


user_view = UserView.as_view('user_view', controller=GetUserController())
app.add_url_rule('/users/<id>', view_func=user_view)


@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    print(json.dumps(user))
    return jsonify(user), 201


@app.route('/users/<user_id>', methods=['PUT'])
def update_resource(user_id):
    user = request.json
    return jsonify(user), 200


@app.route('/users/<user_id>', methods=['PATCH'])
def patch_resource(user_id):
    user = request.json
    key = next(iter(user)) # get the first (and only) key in the dictionary
    return jsonify({key: user[key]}), 200


@app.delete('/users/<user_id>')
def delete_user(user_id) -> Response:
    try:
        controller = DeleteUserController()
        controller.delete(request=user_id)
    except NotImplementedError:
        pass
    return Response(status=204)


@app.post('/users/update')
def update_user() -> Response:
    user = request.json
    try:
        controller = UpdateUserController()
        update_user_request = UpdateUserRequest(user=user)
        controller.update(request=update_user_request)
    except NotImplementedError:
        pass
    return jsonify(user)
