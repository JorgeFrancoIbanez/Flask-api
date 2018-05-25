import argparse

from app import db
from app.models import User
from werkzeug.security import generate_password_hash


parser = argparse.ArgumentParser(description='Add user to the database.')
parser.add_argument('--username', type=str, default='test', help='The username')
parser.add_argument('--email', metavar='N', type=str, default='test@test.com', help='The user email')
parser.add_argument('--password', metavar='N', type=str, default='testtest', help='The user email')

args = parser.parse_args()
if not User.query.all():
    names = ['jorge', 'naty', 'dani']
    emails = ['jorge.franco@gmail.com', 'naty@gmial.com', 'dani@gmail.com']
    for i in range(3):
        print i
        u = User(username=names[i], email=emails[i])
        u.set_password(generate_password_hash('qwe123'))
        db.session.add(u)
        db.session.commit()

else:
    u = User(username=args.username, email=args.email)
    u.set_password(password_hash=generate_password_hash(args.password))
    db.session.add(u)
    db.session.commit()

users = User.query.all()
print users
