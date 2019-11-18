# DynamoDB API
> This is an API that provide simple CRUD into dynamoDB using python.


## Running locally

OS X & Linux & Windows:

```sh
pip install requirements.txt
python app.py
```


## Tests

```sh
cd tests
python test_app.py
```

## Sample requests


**POST**


Create a new item(user, product, etc.)
* ```/api/gianini/{string:tableName}/insert```

Update a item(user, product, etc.) - ON WORKING
* ```/api/gianini/{string:tableName}/update```

Delete a item(user, product, etc.)
* ```/api/gianini/{string:tableName}/delete}```

Query a item(user, product, etc.)
* ```/api/gianini/{string:tableName}/query?chave={string:keyName}&value={string:value}```


## Release History


* 0.0.1
    * Work in progress


## Contributing


Lucas Waiteman Bastos – [@Tracun](https://twitter.com/tracun) – tracuns@gmail.com
https://github.com/tracun/


1. Fork it (<https://github.com/Tracun/dynamoDB_API/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

