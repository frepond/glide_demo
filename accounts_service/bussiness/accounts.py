from accounts_service.extensions import db
from accounts_service.models import Account


def create_account(data):
    email = data.get('email')
    account = Account(email)

    db.session.add(account)
    db.session.commit()

    return account.id


def update_account(account_id, data):
    account = Account.query.filter(Account.id == account_id).one()
    account.email = data.get('email')
    db.session.add(account)
    db.session.commit()


def delete_account(account_id):
    account = Account.query.filter(Account.id == account_id).one()
    db.session.delete(account)
    db.session.commit()
