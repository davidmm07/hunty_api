# hunty_api


The API hunty_api, built with FastApi, perform basic CRUD MongoDB operations with PyMongo .


### :pick: Previous Requirements
* Python
* Pip
* Create a Python Virtual Environment `python3 -m venv ~/.venv` or `virtualenv ~/.venv`
* [Fast Api](https://fastapi.tiangolo.com/).

## How to run

## Installation dependencies

```bash
 pip install --no-cache-dir --upgrade -r requirements.txt
```
add environment variables
```bash
 touch .env
```

### Ways of running the api
#### 1. Run with uvicorn

```bash
uvicorn app:app --reload
```

#### 2. Or run with docker :whale:


1. Run container and check logs with:
```sh
docker-compose up -d && docker-compose logs -f
```

4. Verify that the containers are running
```sh
docker ps 
```

### Swagger section

1. Go to domain below

```sh
 localhost:3000/docs 
```
2. Check tags users and vacancies

