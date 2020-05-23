# Pantry

This is the repository for the pantry app.

## Getting started
This project uses python [Django 3.x](https://docs.djangoproject.com/en/3.0/)

## Dependencies
* [Postgresql](https://postgresapp.com/)
* [Python 3.8.2](https://www.python.org/ftp/python/3.8.2/python-3.8.2-macosx10.9.pkg)

## Setting up the database
Make sure the `psql` command is available

Then run `psql -c "CREATE DATABASE pantry;"` to create the database we will be using.

## Running the backend
*Use a virtual environment*

I recommend [pyenv](https://github.com/pyenv/pyenv) but feel free to use the builtin python `venv` package (just be sure to activate it when you're working on this project)

Install the pip dependencies and run the development server
``` shell
make install
make backend
```

The django backend should now be running on port 8000.

## Running the frontend

``` shell
make install-ui
make ui
```

A frontend dev server should now be built and listening on port 8080. There is a dev configuration that proxies all requests matching '/api' to our django backend.

## Running tests
`python manage.py test pantry`
