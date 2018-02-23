import argparse

from app import db
from app.models import User

parser = argparse.ArgumentParser(description='Add user to the database.')
parser.add_argument('--email', type=str, default=None, help='The user email')

args = parser.parse_args()

users = User.query.all()
print users

for u in users:
    if u.email == 'None':
        db.session.delete(u)
        db.session.commit()
    elif u.email == args.email:
        db.session.delete(u)
        db.session.commit()

users = User.query.all()
print users
