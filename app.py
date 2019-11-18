from flask_restful import Api
from flask import Flask, jsonify, render_template, request

from dynamoDBCrud import DynamoDB

app = Flask(__name__)
api = Api(app)  # api is a collection of objects, where each object contains a specific functionality (GET, POST, etc)

@app.route('/api/gianini/<string:table>/insert', methods=["POST"])
def insert(table):
    dynamoDB = DynamoDB(table)

    if request.is_json:
        data = request.get_json()
        print (data)
        response = dynamoDB.insert(data)
        return jsonify(response)
    else:
        return jsonify(status="Request was not JSON")

@app.route('/api/gianini/<string:table>/update', methods=["POST"])
def update(table):
    dynamoDB = DynamoDB(table)

    if request.is_json:
        data = request.get_json()
        print (data)
        response = dynamoDB.update(data)
        return jsonify(response)
    else:
        return jsonify(status="Request was not JSON")


@app.route('/api/gianini/<string:table>/delete', methods=["POST"])
def delete(table):
    dynamoDB = DynamoDB(table)

    if request.is_json:
        data = request.get_json()
        print (data)
        response = dynamoDB.delete(data)
        return jsonify(response)
    else:
        return jsonify(status="Request was not JSON")


@app.route('/api/gianini/<string:table>/query', methods=["POST"])
def query(table):
    dynamo = DynamoDB(table)
    query_parameters = request.args

    chave = query_parameters['key']
    valor = query_parameters['email']
    print('key={0} & valor={1}'.format(chave, valor))

    if chave == '' or valor == '':
        return jsonify(bad_request(400))

    response = dynamo.query(chave, valor)
    return jsonify(response)

@app.errorhandler(400)
def bad_request(e):
    return {'errors':[{'code':400,'message':'Bad request', 'internalMessage':'{}'.format('Check if all parameters was inputted and non blank')}]}

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()