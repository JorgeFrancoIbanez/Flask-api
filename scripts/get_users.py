from app.models import User


users = User.query.all()
print users

for u in users:
    print(u.email, u.id)
