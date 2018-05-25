import argparse

from app import db
from app.models import Node, Post, User


parser = argparse.ArgumentParser(description='Add user to the database.')
parser.add_argument('--last', metavar='N', type=str, default=True, help='MAC OF THE NODE')

args = parser.parse_args()

if args.last:
    n = Node.query.all()
    db.session.delete(n[len(n)-1])
    db.session.commit()