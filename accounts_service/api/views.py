from flask import Blueprint
from flask_restful import Api

from accounts_service.api.resources import AccountResource, AccountCollection


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(AccountResource, '/accounts/<int:account_id>')
api.add_resource(AccountCollection, '/accounts')
