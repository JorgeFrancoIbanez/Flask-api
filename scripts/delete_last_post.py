import argparse

from app import db
from app.models import Post, User


parser = argparse.ArgumentParser(description='Add user to the database.')
parser.add_argument('--email', type=str, default='jorge.franco@ormuco.com', help='The user email that will delete the post')
parser.add_argument('--last', type=int, help='Delete # latest posts')
parser.add_argument('--recent', type=int, help='Delete # recent posts')

args = parser.parse_args()

user = User.query.filter(User.email == args.email).first()
# posts = Post.query.filter(Post.user_id == user.id).limit(1)
all_posts = Post.query.all()
# p = sorted(all_posts, reverse=True)[:1]
print all_posts[len(all_posts)-1].id
p = all_posts[len(all_posts)-1].id
# posts = Post.select().order_by(all_posts.id.desc()).limit(1)
db.session.delete(all_posts[len(all_posts)-1])
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
