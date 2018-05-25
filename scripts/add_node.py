import argparse

from app import db
from app.models import User, Node

# parser = argparse.ArgumentParser(description='Add user to the database.')
# parser.add_argument('--name', type=str, default='default_name', help='Name of the node')
# parser.add_argument('--email', metavar='N', type=str, default='naty@gmial.com',
#                     help='User that make the request')
# parser.add_argument('--mac', metavar='N', type=str, default='123eqw', help='MAC OF THE NODE')

# parser = argparse.ArgumentParser(description='Add user to the database.')
# parser.add_argument('--name', type=str, default='default_name', help='Name of the node')
# parser.add_argument('--email', metavar='N', type=str, default='jorge.franco@gmail.com',
#                     help='User that make the request')
# parser.add_argument('--mac', metavar='N', type=str, default='MAC1234', help='MAC OF THE NODE')

parser = argparse.ArgumentParser(description='Add user to the database.')
parser.add_argument('--name', type=str, default='Name-juanse-1', help='Name of the node')
parser.add_argument('--email', metavar='N', type=str, default='js.mantilla128@gmail.com',
                    help='User that make the request')
parser.add_argument('--mac', metavar='N', type=str, default='qewwqe', help='MAC OF THE NODE')

args = parser.parse_args()
u = User.query.filter(User.email == args.email).first()
nodes = Node.query.filter(Node.mac == args.mac).all()
if not nodes:
    n = Node(name=args.name, user_id=u.id, mac=args.mac)
    db.session.add(n)
    db.session.commit()

nodes = Node.query.filter(Node.user_id == u.id)

print u.id, 'has: \n'

for node in nodes:
    print node.name, node.mac, node.timestamp
