from app.models import Node, User
from datetime import datetime



nodes = Node.query.all()
print 'List of all on :\n ', datetime.today().date()

for n in nodes:
    user = User.query.filter(User.id == n.user_id).first()
    print n.id, user.username, ':', n.name, 'at : ', n.creation_date
