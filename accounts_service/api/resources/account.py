from flask import request
from flask_restful import Resource, Api

from accounts_service.extensions import db, ma
from accounts_service.models import Account


class AccountSchema(ma.ModelSchema):
    class Meta:
        model = Account
        sqla_session = db.session


class AccountResource(Resource):
    """Single object resource
    """
    def get(self, account_id):
        schema = AccountSchema()
        account = Account.query.get_or_404(account_id)

        return schema.dump(account).data

    def put(self, account_id):
        schema = AccountSchema(partial=True)
        account = Account.query.get_or_404(account_id)
        account, errors = schema.load(request.json, instance=account)
        if errors:
            return errors, 400

        return None, 204

    def delete(self, account_id):
        account = Account.query.get_or_404(account_id)
        db.session.delete(account)
        db.session.commit()

        return None, 204


class AccountCollection(Resource):
    """Creation and get_all
    """

    def get(self):
        schema = AccountSchema(many=True)
        accounts = Account.query.all()
        return schema.dump(accounts).data

    def post(self):
        schema = AccountSchema()
        account, errors = schema.load(request.json)
        if errors:
            return errors, 400

        db.session.add(account)
        db.session.commit()

        # TODO: get path from resource
        return None, 201, {'Location': '%s/%d' % ('/api/v1/accounts', account.id)}
