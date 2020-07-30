from flask_restful import Api
from flask import Flask, jsonify, render_template, request, json
import ast
import decimal

from dynamoDBCrud import DynamoDB

app_dev = Flask(__name__)
api = Api(app_dev)  # api is a collection of objects, where each object contains a specific functionality (GET, POST, etc)
#########################################################################################################
#################################### DEVELOPMENT ONLY ###################################################
#########################################################################################################
@app_dev.route('/api/gianini/<string:table>/insert', methods=["POST"])
def insert(table):
    table = "{0}_{1}".format(table, "dev")
    dynamoDB = DynamoDB(table)

    if request.is_json:
        data = request.get_json()
        print (data)
        if('valueHospital' in data or 'valueRepresentante' in data):
            data['valueHospital'] = decimal.Decimal(str(data['valueHospital']))
            data['valueRepresentante'] = decimal.Decimal(str(data['valueRepresentante']))
            data['quant'] = decimal.Decimal(str(data['quant']))

        elif ('maoObraValue' in data or 'valorVisita' in data):
            data['maoObraValue'] = decimal.Decimal(str(data['maoObraValue']))
            data['valorVisita'] = decimal.Decimal(str(data['valorVisita']))

            if (data['replacedParts'] != None):
                for replacedParts in data['replacedParts']:
                    replacedParts['value'] = decimal.Decimal(str(replacedParts['value']))
                    replacedParts['quant'] = decimal.Decimal(str(replacedParts['quant']))
            
        response = dynamoDB.insert(data)
        return jsonify(response)
    else:
        return jsonify({'message': 'Request was not JSON', 'response': None}), 500

@app_dev.route('/api/gianini/<string:table>/update', methods=["POST"])
def update(table):
    table = "{0}_{1}".format(table, "dev")
    dynamoDB = DynamoDB(table)

    if request.is_json:
        data = request.get_json()
        print (data)
        if('valueHospital' in data or 'valueRepresentante' in data):
            data['valueHospital'] = decimal.Decimal(str(data['valueHospital']))
            data['valueRepresentante'] = decimal.Decimal(str(data['valueRepresentante']))
            data['quant'] = decimal.Decimal(str(data['quant']))
        response = dynamoDB.update(data)
        return jsonify(response)
    else:
        return jsonify({'message': 'Request was not JSON', 'response': None}), 500


@app_dev.route('/api/gianini/<string:table>/delete', methods=["POST"])
def delete(table):
    table = "{0}_{1}".format(table, "dev")
    dynamoDB = DynamoDB(table)

    if request.is_json:
        data = request.get_json()
        print (data)
        response = dynamoDB.delete(data)
        return jsonify(response)
    else:
        return jsonify({'message': 'Request was not JSON', 'response': None}), 500

@app_dev.route('/api/gianini/<string:table>/select', methods=["POST"])
def select(table):
    table = "{0}_{1}".format(table, "dev")
    dynamo = DynamoDB(table)

    print('###### Request: ######', request.get_json())

    if request.is_json:
        data = request.get_json()
        print (data)
        response = dynamo.select(data)
        
        return json.dumps(response, default=decimal_default)
    else:
        return jsonify({'message': 'Request was not JSON', 'response': None}), 500

@app_dev.route('/api/gianini/<string:table>/scan', methods=["POST"])
def scan(table):
    table = "{0}_{1}".format(table, "dev")
    dynamo = DynamoDB(table)

    response = dynamo.scan()
    print (response)
    return json.dumps(response, default=decimal_default)

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

@app_dev.route('/api/gianini/<string:table>/query', methods=["POST"])
def query(table):
    table = "{0}_{1}".format(table, "dev")
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

@app_dev.route('/api/gianini/<string:table>/login', methods=["POST"])
def login(table):
    table = "{0}_{1}".format(table, "dev")
    dynamo = DynamoDB(table)

    print('###### Request: ######', request.get_json())

    if request.is_json:
        data = request.get_json()

        id = data['id']
        
        user = {
            'id':id
        }

        password = data['password']

        response = dynamo.select(user)

        # print("response app_dev.py", response)
        # print("response app_dev.py", response[0])

        if 'id' in response[0]['response'] and response[0]['response']['id'] == id and response[0]['response']['password'] == password:
            return jsonify(response)

        return jsonify({'id':None, 'password':None})
    else:
        return jsonify({'message': 'Request was not JSON', 'response': {}}), 500

@app_dev.errorhandler(400)
def bad_request(e):
    return {'errors':[{'code':400,'message':'Bad request', 'internalMessage':'{}'.format('Check if all parameters was inputted and non blank')}]}

if __name__ == '__main__':
    app_dev.run()
