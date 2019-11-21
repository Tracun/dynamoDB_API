import boto3
from boto3.dynamodb.conditions import Key, Attr
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
		#Convert to dict
		dictItem = ast.literal_eval(item)

		response = self.table.put_item(
		   Item=dictItem
		)
		
		return response
		
	def update(self, item):
		#Convert to dict
		dictItem = ast.literal_eval(item)

		return self.table.update_item(
			Key=dictItem,
			UpdateExpression='SET nomeFantasia = :val1',
			ExpressionAttributeValues={
				':val1': 'Nome fantasia Alterado'
			}
		)
		
	def delete(self, chave):
		#Convert to dict
		try:
			dictChave = ast.literal_eval(chave)
			return self.table.delete_item(
				Key=dictChave
			)
		except Exception as e:
			return {'erro':e}

	def select(self, chave):
		#Convert to dict
		try:
			response = self.table.get_item(
				Key=chave
			)

			if 'Item' in response:
				return response['Item']
			else:
				return {'message':'Not found'}
		except Exception as e:
			print('Erro exception: ', e)
			return {'Erro':e}
		
	def query(self, chave, valor):

		try:
			response = self.table.query(
				KeyConditionExpression=Key(chave).eq(valor)
			)

			if 'Items' in response:
				return response['Items']
			else:
				return {'message':'Not found'}

			# response = self.table.scan(
			# 	FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
			# )
			# items = response['Items']
			# print(items)
		except Exception as e:
			print('Erro exception: ', e)
			return {'Erro':e}