from app.models import User


# users = User.query.filter_by(username='1').first()
users = User.query.all()
# users = User.query.all()
print users

for u in users:
    print(u.email, u.id, u.username, u.password_hash)
