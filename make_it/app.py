from flask import Flask, Response, request, jsonify

from make_it.controllers import AddUserController, AddUserRequest, UpdateUserController, UpdateUserRequest

app = Flask(__name__) #__name__ is a special variable in Python that is set to the name of the current module.


@app.get("/ping")
def ping():
    return Response(status=501)


# Define a GET route
@app.route('/users', methods=['GET'])
def get_resource():
    return Response(status=501)


# Define a POST route
@app.route('/users', methods=['POST'])
def create_resource():
    user = request.json
    return jsonify(user), 201


# Define a DELETE route
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_resource(user_id):
    return Response(status=204)



# Define a PUT route
@app.route('/users/<user_id>', methods=['PUT'])
def update_resource(user_id):
    user = request.json
    return jsonify(user), 200


# Define a PATCH route
@app.route('/users/<user_id>', methods=['PATCH'])
def patch_resource(user_id):
    user = request.json
    key = next(iter(user)) # get the first (and only) key in the dictionary
    return jsonify({key: user[key]}), 200


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
