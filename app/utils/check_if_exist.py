from app.models import Node,  User, Pool


def check_node(data):
    node = Node.query.filter(Node.mac == data).all()
    if not node:
        return False
    else:
        return True


def check_node_pool(pool):
    pool = Pool.query.filter(Node.pool == pool).all()
    if not pool:
        return False
    else:
        return True


def check_user(email):
    user = User.query.filter(User.email == email).all()
    if not user:
        return False
    else:
        return user
