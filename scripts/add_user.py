import argparse

from app import db
from app.models import User

parser = argparse.ArgumentParser(description='Add user to the database.')
parser.add_argument('--username', type=str, default='None', help='The username')
parser.add_argument('--email', metavar='N', type=str, default='None', help='The user email')

args = parser.parse_args()
if not User.query.all():
    names = ['jorge', 'naty', 'dani']
    emails = ['jorge.franco@gmail.com', 'naty@gmial.com', 'dani@gmail.com']
    for i in range(3):
        print i
        u = User(username=names[i], email=emails[i])
        db.session.add(u)
        db.session.commit()

else:
    u = User(username=args.username, email=args.email)
    db.session.add(u)
    db.session.commit()

users = User.query.all()
print users
