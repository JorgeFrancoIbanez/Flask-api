from app import db
from datetime import datetime
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(140))
    # timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    timestamp = db.Column(db.DateTime(timezone=True), index=True, server_default=func.now())
    creation_date = db.Column(db.Date, index=True, server_default=datetime.today().strftime('%Y-%m-%d'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    node_id = db.Column(db.Integer, db.ForeignKey('node.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.message)


class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    creation_date = db.Column(db.Date, index=True, default=datetime.today().date())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    mac = db.Column(db.String(140))

    def __repr__(self):
        return '<Node {}>'.format(self.name)


