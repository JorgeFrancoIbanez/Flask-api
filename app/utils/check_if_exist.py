from app.models import Node,  User


def check_node(mac):
    node = Node.query.filter(Node.mac == mac).all()
    if not node:
        return False
    else:
        return True


def check_user(email):
    user = User.query.filter(User.email == email).all()
    if not user:
        return False
    else:
        return user
