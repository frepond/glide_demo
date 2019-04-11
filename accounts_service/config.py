"""Default configuration

Use env var to override
"""
DEBUG = True
SECRET_KEY = "changeme"

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/accounts_service.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
