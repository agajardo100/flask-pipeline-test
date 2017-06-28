from __future__ import absolute_import
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

from . import db, login_manager, flask_bcrypt


"""
Define User Model
"""
class User(UserMixin, db.Model):

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    _password = db.Column(db.Binary(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, first_name, last_name, username, email, pw):
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self._password = pw

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')


    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        print "PasswordSet"
        self._password = flask_bcrypt.generate_password_hash(password)


    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return flask_bcrypt.check_password_hash(self._password, password.encode('utf-8'))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))