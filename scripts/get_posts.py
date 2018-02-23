from app.models import Post, User


posts = Post.query.all()
print 'List of all :\n '
print User.query.filter(User.id == 1).first()
for p in posts:
    user = User.query.filter(User.id == p.user_id).first()
    print p.id, user.username, ':', p.message, 'at : ', p.creation_date
