import argparse

from app import db
from app.models import Node, Post

all_posts = Post.query.all()
all_nodes = Node.query.all()

for i in all_posts:
    db.session.delete(i)
    db.session.commit()

for i in all_nodes:
    db.session.delete(i)
    db.session.commit()


# for u in users:
#     if u.email == 'None':
#         db.session.delete(u)
#         db.session.commit()
#     elif u.email == args.email:
#         db.session.delete(u)
#         db.session.commit()
#
# users = User.query.all()
# print users
#
#
#
# for p in posts:
#     print user.username, ':', p.message
