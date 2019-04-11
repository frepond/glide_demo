import re
from accounts_service.extensions import db
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import validates


class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(EmailType, nullable=False)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<Account %r>' % self.email

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not an email address')

        return email
