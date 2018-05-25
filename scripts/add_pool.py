import argparse

from app import db
from app.models import Pool

parser = argparse.ArgumentParser(description='Add user to the database.')
parser.add_argument('--name', type=str, default='QR recognition message', help='Name of the node')
parser.add_argument('--repository', metavar='N', type=str, default='https://github.com/JorgeFrancoIbanez/qrreader',
                    help='User that make the request')
args = parser.parse_args()
pools = Pool.query.all()
if not pools:
    p = Pool(name=args.name, repository=args.repository)
    db.session.add(p)
    db.session.commit()

for pool in pools:
    print pool.name, pool.repository
