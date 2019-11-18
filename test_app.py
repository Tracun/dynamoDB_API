import requests

api_url_base = 'http://localhost:5000'
endPoint = '/api/gianini'

def testInsertUsers():
    user = "{'email':'contato@amandagianini.com', 'cnpj':'15047359000191', 'password':'amanda'}"
    response = requests.post(api_url_base + endPoint + '/{0}/{1}'.format('Users', 'insert'), json=user)

    assert(response.json()['ResponseMetadata']['HTTPStatusCode'] == 200)

def testDeleteUsers():
    user = "{'email':'contato@amandagianini.com', 'cnpj':'15047359000191'}"
    
    response = requests.post(api_url_base + endPoint + '/{0}/{1}'.format('Users', 'delete'), json=user)

    assert(response.json()['ResponseMetadata']['HTTPStatusCode'] == 200)

def testQueryUsers():
    response = requests.post(api_url_base + endPoint + '/{0}/{1}?{2}&{3}'.format('Users', 'query', 'key=email', 'email=tracuns@gmail.com'))

    assert(response.json()[0]['cnpj'] == '1234567890123')

def testUpdateUsers(ticker):
    user = "{'email':'contato@amandagianini.com', 'cnpj':'15047359000191'}"

    response = requests.post(api_url_base + endPoint + '/{0}/{1}'.format('Users', 'update'), json=user)

    assert(response.json()['ResponseMetadata']['HTTPStatusCode'] == 200)

if __name__ == '__main__':

    testInsertUsers()
    testQueryUsers()
    testDeleteUsers()
    
    # testUpdateUsers()