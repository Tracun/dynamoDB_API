import requests

api_url_base = 'http://localhost:5000'
endPoint = '/api/gianini'


def testInsert():
    data = {
        "address": {
            "cep": "02994000",
            "city": "Sao paulo",
            "neighborhood": "Jardim bandeirantes",
            "number": "312",
            "state": "Sao Paulo",
            "street": "Alto do Rio bravo"
        },
        "cellphone": "9999999999",
        "cnpj": "09876543211234",
        "email": "gostoDaMonica@eu.com",
        "name": "Hospital Cebolinha",
        "phone": "1143564345"
    }

    response = requests.post(api_url_base + endPoint +
                             '/{0}/{1}'.format('Clients', 'insert'), json=data)

    assert(response.json()[0]['response']['ResponseMetadata']['HTTPStatusCode'] == 200)


def testDelete():
    data = "{'cnpj':'09876543211234'}"

    response = requests.post(api_url_base + endPoint +
                             '/{0}/{1}'.format('Clients', 'delete'), json=data)

    print(response.json())
    # assert(response.json()['ResponseMetadata']['HTTPStatusCode'] == 200)


def testQueryUsers():
    response = requests.post(api_url_base + endPoint + '/{0}/{1}?{2}&{3}'.format(
        'Clients', 'query', 'key=cnpj', 'value=38161933000133'))

    assert(response.json()[0]['cnpj'] == '38161933000133')


def testUpdateUsers():
    user = "{'cnpj':'15047359000191', 'email':'contato@amandagianini.com'}"

    response = requests.post(api_url_base + endPoint +
                             '/{0}/{1}'.format('Users', 'update'), json=user)

    assert(response.json()['ResponseMetadata']['HTTPStatusCode'] == 200)


def testQuerySchedulingDates():
    response = requests.post(api_url_base + endPoint + '/{0}/{1}?{2}&{3}'.format(
        'SchedulingDates', 'query', 'key=date', 'value=27112019'))

    print(response.json()[0])
    assert(response.json()[0]['cnpj'] == '38161933000133')


def testSelect():
    data = {'date': '27112019', 'hour': '0700'}

    response = requests.post(
        api_url_base + endPoint + '/{0}/{1}'.format('SchedulingDates', 'select'), json=data)
    print(response.json)

    assert(response.json()['date'] == '27112019')


def testScan():

    response = requests.post(api_url_base + endPoint +
                             '/{0}/{1}'.format('SchedulingDates', 'scan'))
    print(response.json)

    # assert(response.json()['date'] == '27112019')


def testLogin():
    user = {'cnpj': '123456789', 'password': '1234'}
    response = requests.post(
        api_url_base + '/api/gianini/Users/login', json=user)

    assert(response.json()['cnpj'] == '123456789')
    assert(response.json()['email'] == 'tracuns@gmail.com')
    assert(response.json()['password'] == '1234')


if __name__ == '__main__':

    testScan()
    # testSelect()
    # testQuerySchedulingDates()
    # testLogin()
    testInsert()
    # testQueryUsers()
    testDelete()

    # testUpdateUsers()
