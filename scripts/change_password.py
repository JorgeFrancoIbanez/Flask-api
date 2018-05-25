import argparse

from app import db
from app.models import User

email="jorge.franco@gmail.com"
password="qweqwe123123"
u = User.query.filter(User.email == email).first()

print(u.email, 'password: \n', u.password_hash)
u.set_password(password)
print(u.email, 'password: \n', u.password_hash)
db.session.add(u)
db.session.commit()