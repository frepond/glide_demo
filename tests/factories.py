from accounts_service.models import Account


def account_factory(i):
    return Account(
        email="user{}@mail.com".format(i)
    )
