from flask_restful import Api
from flask import Flask, jsonify, render_template, request, json
import ast

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
        return jsonify({'message': 'Request was not JSON', 'response': None}), 500

@app.route('/api/gianini/<string:table>/update', methods=["POST"])
def update(table):
    dynamoDB = DynamoDB(table)

    if request.is_json:
        data = request.get_json()
        print (data)
        response = dynamoDB.update(data)
        return jsonify(response)
    else:
        return jsonify({'message': 'Request was not JSON', 'response': None}), 500


@app.route('/api/gianini/<string:table>/delete', methods=["POST"])
def delete(table):
    dynamoDB = DynamoDB(table)

    if request.is_json:
        data = request.get_json()
        print (data)
        response = dynamoDB.delete(data)
        return jsonify(response)
    else:
        return jsonify({'message': 'Request was not JSON', 'response': None}), 500

@app.route('/api/gianini/<string:table>/select', methods=["POST"])
def select(table):
    dynamo = DynamoDB(table)

    print('###### Request: ######', request.get_json())

    if request.is_json:
        data = request.get_json()
        print (data)
        response = dynamo.select(data)
        return jsonify(response)
    else:
        return jsonify({'message': 'Request was not JSON', 'response': None}), 500

@app.route('/api/gianini/<string:table>/scan', methods=["POST"])
def scan(table):
    dynamo = DynamoDB(table)

    response = dynamo.scan()
    print (response)
    return jsonify(response)

@app.route('/api/gianini/<string:table>/query', methods=["POST"])
def query(table):
    dynamo = DynamoDB(table)
    query_parameters = request.args

    chave = query_parameters['key']
    valor = query_parameters['value']
    print('key={0} & valor={1}'.format(chave, valor))

    if chave == '' or valor == '':
        return jsonify(bad_request(400))

    response = dynamo.query(chave, valor)
    print(response)
    return jsonify(response)

@app.route('/api/gianini/Users/login', methods=["POST"])
def login():
    dynamo = DynamoDB('Users')

    print('###### Request: ######', request.get_json())

    if request.is_json:
        data = request.get_json()

        cnpj = data['cnpj']
        
        user = {
            'cnpj':cnpj
        }

        password = data['password']

        response = dynamo.select(user)

        print("response aap.py", response)
        print("response aap.py", response[0])

        if 'cnpj' in response[0]['response'] and response[0]['response']['cnpj'] == cnpj and response[0]['response']['password'] == password:
            return jsonify(response)

        return jsonify({'cnpj':None, 'password':None})
    else:
        return jsonify({'message': 'Request was not JSON', 'response': {}}), 500

@app.errorhandler(400)
def bad_request(e):
    return {'errors':[{'code':400,'message':'Bad request', 'internalMessage':'{}'.format('Check if all parameters was inputted and non blank')}]}

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()