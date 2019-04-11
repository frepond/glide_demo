from flask_restplus import fields
from accounts_service.api.restplus import api

account = api.model('Account', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an account'),
    'email': fields.String(required=True, description='Email'),
})
