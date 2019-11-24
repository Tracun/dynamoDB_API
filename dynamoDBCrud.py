import boto3
from boto3.dynamodb.conditions import Key, Attr
from flask import jsonify, json
import sys
import ast

class DynamoDB():

	SERVICE = 'dynamodb'
	TABLE = 'Users'

	def __init__(self, table):
		# Get the service resource.
		self.dynamodb = boto3.resource(self.SERVICE)

		# Instantiate a table resource object without actually
		# creating a DynamoDB table. Note that the attributes of this table
		# are lazy-loaded: a request is not made nor are the attribute
		# values populated until the attributes
		# on the table resource are accessed or its load() method is called.
		self.table = self.dynamodb.Table(table)

	def insert(self, item):
		try:
			response = self.table.put_item(
				Item=item
			)
			
			print(type(item))
			return {'message': 'Created', 'response': response}, 201
			# return response
		except Exception as e:
			print('Erro exception: ', e)
			return {'message': 'Error on insert', 'response': None}, 500
		
	def update(self, item):

		return self.table.update_item(
			Key=item,
			UpdateExpression='SET nomeFantasia = :val1',
			ExpressionAttributeValues={
				':val1': 'Nome fantasia Alterado'
			}
		)
		
	def delete(self, chave):
		
		try:
			
			response = self.table.delete_item(
				Key=chave
			)

			return {'message': 'Deleted', 'response': response['Item']}, 200
		except Exception as e:
			{'message': 'Erro on delete'+e, 'response': None}, 500

	def select(self, chave):
		
		try:
			response = self.table.get_item(
				Key=chave
			)

			if 'Item' in response:
				print('####', response['Item'])
				return {'message': 'Selected', 'response': response['Item']}, 200
			else:
				return {'message': 'Not found', 'response': None}, 500
		except Exception as e:
			print('Erro exception: ', e)
			return {'message': 'Erro on select', 'response': None}, 500
		
	def query(self, chave, valor):

		try:
			response = self.table.query(
				KeyConditionExpression=Key(chave).eq(valor)
			)

			if 'Items' in response:
				return {'message': 'Selected', 'response': response['Items']}, 200
			else:
				return {'message': 'Not found', 'response': None}, 500

			# response = self.table.scan(
			# 	FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
			# )
			# items = response['Items']
			# print(items)
		except Exception as e:
			return {'message': 'Erro on query', 'response': None}, 500