

# FastAPI 
## Introduction
[FastAPI](https://fastapi.tiangolo.com/)
is a web framework for building APIs with Python.
It can run on Python 3.6+ versions. Advantages of FastAPI includes:
* It is fast because of its ASGI layer contarary to WSGI layer as in Flask.
* Provides Validations
* Provides better documentations, which can be accessed using /docs and /redoc
* Supports asynchronous code and concurrency
* Light weight and the code is compact
Uvicorn is the webserver gateway interface used by FastAPI.  
## Installation
#### Basic packages that needs to be installed 
* pip install fastapi     
* pip install uvicorn 
#### Additional packages that needs to be installed when required
Packages for data validations
* pip install pydantic
* pip install Enum
Package for returning HTML response
* pip install jinja2
Package for uploading files and submiting form data
* pip install python-multipart
## Examples
#### Get started with FastAPI
* intro.py shows how to write a basic GET request and how to pass parameters through path and as query. 
* FastAPI can be run from terminal using:
```bash
uvicorn main:app
```
#### Use of Enum
* Enum is helps in forcing given values into one of the required fields. 
* enum.py is an example for the same and also includes the use of type hints in FastAPI

#### Requests using FastAPI
* req.py is an example on how to create endpoints for different requests in FastAPI

#### Use of pydantic
* Pydantic is used for data validations in FastAPI
* pydan.py is an exmaple for the same

#### Giving HTML page as response
* htmlres.py show how to render HTML page as the reponse.
* Jinja2 needs to be installed for the same.

#### Accessing uploaded files and form data using FastAPI
* accform.py shows how to access form data and on how to recieve the uploaded files from client


