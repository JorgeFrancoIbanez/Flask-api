from app import db
from app import login

from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    timestamp = db.Column(db.DateTime(timezone=True), index=True, server_default=func.now())
    profile_image = db.Column(db.LargeBinary)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(140))
    node_id = db.Column(db.Integer, db.ForeignKey('node.id'))
    timestamp = db.Column(db.DateTime(timezone=True), index=True, server_default=func.now())

    def __init__(self, message, node_id):
        self.message = message
        self.node_id = node_id

    def __repr__(self):
        return '<Post {}>'.format(self.message)


class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(140))
    name = db.Column(db.String(140))
    pool_id = db.Column(db.Integer, db.ForeignKey('pool.id'))
    timestamp = db.Column(db.DateTime(timezone=True), index=True, server_default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, mac, name, pool_id, user_id):
        self.mac = mac
        self.name = name
        self.pool_id = pool_id
        self.user_id = user_id

    def __repr__(self):
        return '<Node {}>'.format(self.name)


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(140))
    pool_id = db.Column(db.Integer, db.ForeignKey('pool.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __repr__(self):
        return '<Node {}>'.format(self.name)


class Pool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime(timezone=True), index=True, server_default=func.now())
    repository = db.Column(db.String(140))

    def __init__(self, name, repository):
        self.name = name
        self.repository = repository

    def __repr__(self):
        return '<Node {}>'.format(self.name)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
