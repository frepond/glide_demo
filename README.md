# Glide Demo

# accounts_service

Basic account service for Glide demo.

This project was created using `cookiecutter` template ()[https://github.com/karec/cookiecutter-flask-restful] and slightly modified to fit the needs of the demo.

## Setup

First install [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) for easy python virtual environment handling. Then:

```bash
mkvirtualenv glide_demo -p $(which python3)
pip install -r requirements.txt
```

## Run the tests

```bash
pip install -r requirements_test.txt
tox
```

## Run from the sources

You first need to setup the database:

```bash
PYTHONPATH=. python accounts_service/manage.py init
```

Then just run the app:

```bash
PYTHONPATH=. python accounts_service/manage.py run
```

The `manage.py` supports a few additional commands, just run it without arguments. There is an (Insomnia)[https://insomnia.rest] bundle to test the api. Just download the app and import the bundle.


__Warning__: the `init` command drops the database if it exists.

## Run from docker

Build the docker image:

```bash
docker build -t glide_demo .
```

The just run:

```bash
docker run -p 5000:5000 glide_demo
```

__Warning__: you need docker installed. The database is not persisted.

## Considerations

- I started with boilerplate code after reviewing a few cookiecutter templates I stick with this, because I found it, well structured and simple enough for the challenge (flask-restful for the api + sql-alchemy for accessing the db + validation).
- Even when the front end should have email validation (in order to provide early feedback to the user) the service layer must validate because UI could be one of the many API clients.
- The demo uses Sqlite3 which is suitable for testing, given that we're using an ORM like SQLAchemy moving to Postgres should be trivial in this case (no complicated queries, no stored procedures, etc.)

## TODO

- Development/Staging/Production config
- Packaging
- Security
- Set correct headers on POST/PUT response
- Better error handling and descriptions (e.g. which field failed to validate)
- Localization
- Search & pagination
- Logging
- Audit trail
- As always better and more tests! (only basic tests at at rest api level)
- Improve swagger doc (better comments, remove `id` form post/put)
- Schema migration handling
- ...
