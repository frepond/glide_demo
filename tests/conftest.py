import json

import pytest
from accounts_service.app import create_app
from accounts_service.extensions import db as _db
from accounts_service.models import Account


@pytest.fixture(scope='session')
def app():
    app = create_app(testing=True)
    return app


@pytest.fixture(scope='session')
def db(app):
    _db.app = app

    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()
