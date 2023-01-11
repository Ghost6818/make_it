from flask import Flask, Response, request, render_template

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




