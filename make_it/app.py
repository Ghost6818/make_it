from flask import Flask, Response, request, jsonify

from make_it.controllers import AddUserController, AddUserRequest, UpdateUserController, UpdateUserRequest, GetUsersController, PutUserController, PatchUserController, DeleteUserController
from make_it.repositories import UserRepository
from make_it.domain import AddUserRequest, GetUsersRequest, PutUserRequest, PatchUserRequest, DeleteUserRequest

app = Flask(__name__) #__name__ is a special variable in Python that is set to the name of the current module.


@app.get("/ping")
def ping():
    return Response(status=501)

@app.post("/users")
def add_user() -> Response:
    controller = AddUserController()
    controller.add(request=AddUserRequest(json=request.json))
    return jsonify(request.json), 201

# Define a GET route
@app.get("/users")
def get_resource()-> Response:
    controller = GetUsersController()
    response = controller.get(request=GetUsersRequest())
    return jsonify(response), 501


# Define a POST route
@app.route('/api/resource', methods=['POST'])
def create_resource():
    return Response(status=501)


# Define a DELETE route
@app.delete("/users/<id>")
def delete_resource(id: int) -> Response:
    controller = DeleteUserController()
    controller.delete(request=DeleteUserRequest(id=id))
    return "", 204


# Define a PUT route
@app.put("/users/<id>")
def put_user(id: int) -> Response:
    controller = PutUserController()
    response = controller.put(request=PutUserRequest(id=id, json=request.json))
    return jsonify(response), 200


# Define a PATCH route
@app.patch("/users/<id>")
def patch_resource(id: int) -> Response:
    controller = PatchUserController()
    response = controller.patch(request=PatchUserRequest(id=id, json=request.json))
    return jsonify(response), 200


@app.post('/users')
def create_user() -> Response:
    user = request.json
    repository = UserRepository()
    controller = AddUserController(repository)
    add_user_request = AddUserRequest(user=user)
    controller.add(request=add_user_request)
    return jsonify(user)


@app.post('/users/update')
def update_user() -> Response:
    user = request.json
    controller = UpdateUserController()
    update_user_request = UpdateUserRequest(user=user)
    controller.update(request=update_user_request)
    return jsonify(user)
