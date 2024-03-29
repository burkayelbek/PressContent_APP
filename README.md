﻿# PressContent Project

## Requirements in the App

* Python 3.10
* PostgreSQL 14
* .env file in the project

## Description
This project is built django rest framework with similarity of press content.

## Installation

Installation on local easy with requirements.txt file:

#### Example .env file content:
* SECRET_KEY='<secret_key>'
* POSTGRES_DB=denebunudb
* POSTGRES_HOST=localhost
* POSTGRES_USER=postgres
* POSTGRES_PASSWORD=<your_password>
* POSTGRES_PORT=5432

And after that

```shell
$ virtualenv -p python3 venv
$ source venv/bin/activate (In Linux)
$ venv/Scripts/activate (In Windows)
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver 8000
```
