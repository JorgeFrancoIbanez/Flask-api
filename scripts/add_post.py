import argparse

from app import db
from app.models import User, Post

parser = argparse.ArgumentParser(description='Add user to the database.')
parser.add_argument('--message', type=str, default='ey mysql areyouthere?', help='message for the post action')
parser.add_argument('--email', metavar='N', type=str, default='jorgefrancoibanez@gmail.com', help='User that make the request')
parser.add_argument('--node', metavar='N', type=int, default=2, help='Node id')

args = parser.parse_args()
u = User.query.filter(User.email == args.email).first()

p = Post(message=args.message, user_id=u.id, node_id=args.node)
db.session.add(p)
db.session.commit()

m = Post.query.filter(Post.user_id == u.id)

for i in m:

    print(u.id, 'with message: \n', i.message, i.timestamp)
