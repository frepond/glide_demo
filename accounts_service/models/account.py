import re
from accounts_service.extensions import db
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import validates


class Account(db.Model):
    """Basic user model
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(EmailType, nullable=False)

    def __init__(self, **kwargs):
        super(Account, self).__init__(**kwargs)

    def __repr__(self):
        return "<Account %s>" % self.email

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not an email address')

        return email
