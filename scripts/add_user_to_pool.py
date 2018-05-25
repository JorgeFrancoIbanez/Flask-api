import argparse

from app import db
from app.models import UserPool
from werkzeug.security import generate_password_hash


parser = argparse.ArgumentParser(description='Add user to the database.')
parser.add_argument('--node', type=str, default='2', help='The username')
parser.add_argument('--pool', metavar='N', type=str, default='1', help='The user email')
parser.add_argument('--user', metavar='N', type=str, default='1', help='The user email')
args = parser.parse_args()

u = UserPool(node_id=args.node, pool_id=args.pool, user_id=args.user)
db.session.add(u)
db.session.commit()

users = UserPool.query.all()
print users
