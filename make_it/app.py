from flask import Flask, Response, request, render_template

app = Flask(__name__) #__name__ is a special variable in Python that is set to the name of the current module.


@app.get("/ping")
def ping():
    return Response(status=501)


# Define a GET route
@app.route('/api/resource', methods=['GET'])
def get_resource():
    resource = render_template()
    return Response(response=resource.to_json(), status=200, mimetype='application/json')


# Define a POST route
@app.route('/api/resource', methods=['POST'])
def create_resource():
    data = request.get_json()
    resource = create_resource(data)
    return Response(response=resource.to_json(), status=201, mimetype='application/json')


# Define a DELETE route
@app.route('/api/resource/<resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    delete_resource(resource_id)
    return Response(status=204)


# Define a PUT route
@app.route('/api/resource/<resource_id>', methods=['PUT'])
def update_resource(resource_id):
    data = request.get_json()
    resource = update_resource(resource_id, data)
    return Response(response=resource.to_json(), status=200, mimetype='application/json')


# Define a PATCH route
@app.route('/api/resource/<resource_id>', methods=['PATCH'])
def patch_resource(resource_id):
    data = request.get_json()
    resource = patch_resource(resource_id, data)
    return Response(response=resource.to_json(), status=200, mimetype='application/json')




