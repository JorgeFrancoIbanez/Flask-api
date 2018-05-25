
from app import app
from app import db
from app.models import User

users = User.query.all()
print users
