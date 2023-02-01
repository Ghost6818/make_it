from flask import Flask, Response, request, jsonify

from make_it.controllers import AddUserController, AddUserRequest, UpdateUserController, UpdateUserRequest

app = Flask(__name__) #__name__ is a special variable in Python that is set to the name of the current module.


@app.get("/ping")
def ping():
    return Response(status=501)


# Define a GET route
@app.route('/api/resource', methods=['GET'])
def get_resource():
    return Response(status=501)


# Define a POST route
@app.route('/api/resource', methods=['POST'])
def create_resource():
    return Response(status=501)


# Define a DELETE route
@app.route('/api/resource/<resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    return Response(status=501)


# Define a PUT route
@app.route('/api/resource/<resource_id>', methods=['PUT'])
def update_resource(resource_id):
    return Response(status=501)


# Define a PATCH route
@app.route('/api/resource/<resource_id>', methods=['PATCH'])
def patch_resource(resource_id):
    return Response(status=501)


@app.post('/users')
def create_user() -> Response:
    user = request.json
    controller = AddUserController()
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
