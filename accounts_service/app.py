from flask import Blueprint, Flask

from accounts_service.api.endpoints.accounts import ns as accounts_ns
from accounts_service.api.restplus import api
from accounts_service.extensions import db, migrate
from flask_cors import CORS


def create_app(config=None, testing=False, cli=False):
    """Application factory, used to create application
    """
    app = Flask('accounts_service')

    configure_app(app, testing)
    configure_extensions(app, cli)
    register_blueprints(app)
    cors = CORS(app, resources={r"/api/v1*": {"origins": "*"}}, expose_headers=['Location'])

    return app


def configure_app(app, testing=False):
    """set configuration for application
    """
    # default configuration
    app.config.from_object('accounts_service.config')

    if testing is True:
        # override with testing config
        app.config.from_object('accounts_service.configtest')
    else:
        # override with env variable, fail silently if not set
        app.config.from_envvar("ACCOUNTS_SERVICE_CONFIG", silent=True)


def configure_extensions(app, cli):
    """configure flask extensions
    """
    db.init_app(app)

    if cli is True:
        migrate.init_app(app, db)


def register_blueprints(app):
    """register all blueprints for application
    """
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(blueprint)
    api.add_namespace(accounts_ns)
    app.register_blueprint(blueprint)
