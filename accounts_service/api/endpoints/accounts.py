import logging

from flask import jsonify, request
from flask_restplus import Resource

from accounts_service.bussiness.accounts import (create_account,
                                                    delete_account,
                                                    update_account)
from accounts_service.api.serializers.accounts import account
from accounts_service.api.restplus import api
from accounts_service.models.accounts import Account

log = logging.getLogger(__name__)

ns = api.namespace('accounts', description='Accounts API')


@ns.route('')
class AccountsCollection(Resource):

    @api.marshal_list_with(account)
    def get(self):
        """
        Returns the list of accounts
        """
        accounts = Account.query.all()

        return accounts

    @api.response(201, 'Account successfully created.')
    @api.expect(account)
    def post(self):
        """
        Creates a new account
        """
        data = request.json
        id = create_account(data)

        return None, 201, {'Location': '%s/%d' % (api.url_for(self), id)}


@ns.route('/<int:id>')
@api.response(404, 'Account not found.')
class AccountItem(Resource):

    @api.marshal_with(account)
    def get(self, id):
        """
        Returns an account with the given id
        """
        return Account.query.filter(Account.id == id).one()

    @api.expect(account)
    @api.response(204, 'Account successfully updated.')
    def put(self, id):
        """
        Updates a account's email.

        Use this method to change the email of an account.

        * Send a JSON object with the new email in the request body.

        ```
        {
          "email": "New email"
        }
        ```

        * Specify the ID of the account to modify in the request URL path.
        """
        data = request.json
        update_account(id, data)

        return None, 204

    @api.response(204, 'Account successfully deleted.')
    def delete(self, id):
        """
        Deletes an account
        """
        delete_account(id)
        return None, 204
