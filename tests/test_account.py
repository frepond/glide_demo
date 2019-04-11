from urllib import parse

import factory
from accounts_service.models import Account
from pytest_factoryboy import register


@register
class AccountFactory(factory.Factory):
    email = factory.Sequence(lambda n: 'user%d@mail.com' % n)

    class Meta:
        model = Account


def test_get_account(client, db, account):
    # test 404
    rep = client.get("/api/v1/accounts/100000")
    assert rep.status_code == 404

    db.session.add(account)
    db.session.commit()

    # test get_account
    rep = client.get('/api/v1/accounts/%d' % account.id)
    assert rep.status_code == 200

    data = rep.get_json()
    assert data['email'] == account.email


def test_put_account(client, db, account):
    # test 404
    rep = client.put("/api/v1/accounts/100000")
    assert rep.status_code == 404

    db.session.add(account)
    db.session.commit()

    new_email = 'new@mail.com'
    data = {'email': new_email}

    # test update account
    rep = client.put('/api/v1/accounts/%d' % account.id, json=data)
    assert rep.status_code == 204

    rep = client.get('/api/v1/accounts/%d' % account.id)
    assert rep.status_code == 200

    data = rep.get_json()
    assert data['email'] == new_email


def test_delete_account(client, db, account):
    # test 404
    rep = client.put("/api/v1/accounts/100000")
    assert rep.status_code == 404

    db.session.add(account)
    db.session.commit()

    # test get_account
    account_id = account.id
    rep = client.delete('/api/v1/accounts/%d' % account_id)
    assert rep.status_code == 204
    assert db.session.query(Account).filter_by(id=account_id).first() is None


def test_create_account(client, db):
    # test bad data
    data = {
        'email': 'bad_email'
    }
    rep = client.post('/api/v1/accounts', json=data)
    assert rep.status_code == 400

    data['email'] = 'create@mail.com'

    rep = client.post('/api/v1/accounts', json=data)
    assert rep.status_code == 201
    assert '/accounts/' in rep.headers['Location']

    resource_path = parse.urlparse(rep.headers['Location']).path
    account_id = resource_path.split('/')[-1]
    account = db.session.query(Account).filter_by(id=account_id).first()
    assert account.email == 'create@mail.com'


def test_get_all_account(client, db, account_factory):
    accounts = account_factory.create_batch(30)

    db.session.add_all(accounts)
    db.session.commit()

    rep = client.get('/api/v1/accounts')
    assert rep.status_code == 200

    results = rep.get_json()
    for account in accounts:
        assert any(u['id'] == account.id for u in results)
