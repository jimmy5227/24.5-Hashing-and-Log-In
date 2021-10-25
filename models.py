"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String, nullable=False)
    username = db.Column(db.String(30), db.ForeignKey(
        'users.username'), nullable=False)

    user = db.relationship('User', backref='feedback')


class User(db.Model):
    __tablename__ = 'users'

    def __repr__(self):
        u = self
        return f'<username: {u.username}, email: {u.email}, first_name: {u.first_name}, last_name: {u.last_name}>'

    username = db.Column(db.String(20), unique=True,
                         primary_key=True, autoincrement=False, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    @classmethod
    def register(cls, username, pwd, email, first_name, last_name):
        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode('utf8')

        return cls(username=username, password=hashed_utf8, email=email, first_name=first_name, last_name=last_name)

    @classmethod
    def authenticate(cls, username, pwd):
        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            return u
        else:
            return False
