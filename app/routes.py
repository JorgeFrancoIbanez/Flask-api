import json

import os

import config
from werkzeug.datastructures import CombinedMultiDict

from app import app
from app import db
from app.forms import AttachNode, DetachNode, LoginForm, ObjectForm, RegistrationForm
from app.utils.convert_json import data_to_json
from app.utils.check_if_exist import check_node, check_user
from app.models import Node, Object, Pool, Post, User
from flask import flash, jsonify, redirect, render_template, request, send_file, url_for
from flask_login import current_user, login_required, login_user, logout_user
from flask_qrcode import QRcode
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

from werkzeug.urls import url_parse
from app.utils.allowed_files import allowed_file
from werkzeug.utils import secure_filename
from base64 import b64encode, b64decode
from werkzeug.security import generate_password_hash, check_password_hash


qrcode = QRcode(app)


@app.route('/')
@app.route('/index')
def index():
    title = 'Cam application'
    if current_user.is_authenticated:
        return render_template('index.html', title=title)
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    print "comes"
    if current_user.is_authenticated:
        print "authenticated"
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    print "end"
    return render_template('/access/login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/monitor-test')
@login_required
def cams():
    posts = Post.query.limit(15).all()
    data = data_to_json(posts)
    return render_template('table.html', title='Camera monitoring system', data_table=data)


@app.route('/nodes/<user_id>', methods=['GET', 'POST'])
def nodes(user_id):
    if request.method == 'GET':
        data = data_to_json(Node.query.limit(15).all())
        print jsonify(data)
        return render_template('nodes.html', title='List of nodes availables', nodes=data)
    if request.method == 'POST':
        data = json.loads(request.data)
        print user_id, data
        if not check_node(data["mac"]):
            n = Node(name=data["name"], user_id=user_id, mac=data["mac"])
            db.session.add(n)
            db.session.commit()
            return 'node successfully added'
        else:
            return 'node already exist'


@app.route('/node/<node_id>', methods=['GET', 'POST'])
def node(node_id):
    if request.method == 'GET':
        data = Node.query.filter(Node.id == node_id).first()
        data_user = User.query.filter(User.id == data.user_id).first()
        print data
        if data.pool_id:
            data_pool = Pool.query.filter(Pool.id == data.pool_id).first()
            data_post = data_to_json(Post.query.filter(Post.node_id == data.id).all())
            return render_template('node.html', nodes=data, pool=data_pool, data_table=data_post, title='Node {}'.format(data.name), user_info=data_user)
        else:
            return render_template('node.html', nodes=data, title='Node {}'.format(data.name), user_info=data_user)
    # if request.method == 'POST':
        # data = json.loads(request.data)
        # print user_id, data
        # if not check_node(data["mac"]):
        #     n = Node(name=data["name"], user_id=user_id, mac=data["mac"])
        #     db.session.add(n)
        #     db.session.commit()
        #     return 'node successfully added'
        # else:
        #     return 'node already exist'


@app.route('/pool/<pool_id>/nodes', methods=['GET', 'POST'])
def nodes_on_pool(pool_id, user_id):
    if request.method == 'GET':
        data = data_to_json(pool_id.query.limit(15).all())
        print jsonify(data)
        return render_template('nodes.html', title='List of nodes availables', nodes=data)
    if request.method == 'POST':
        data = json.loads(request.data)
        print user_id, data
        if not check_node(data["mac"]):
            n = Node(name=data["name"], user_id=user_id, mac=data["mac"])
            db.session.add(n)
            db.session.commit()
            return 'node successfully added'
        else:
            return 'node already exist'


@app.route('/pool/<pool_id>', methods=['GET', 'POST'])
def pool(pool_id, obj=None):
    # user_data = data_to_json(UserPool.query.filter(Pool.id == pool_id).limit(15).all())
    pool_data = Pool.query.filter_by(id=pool_id).first()
    post_data = data_to_json(Post.query.filter(Pool.id == pool_id).limit(15).all())
    node_data = data_to_json(Node.query.filter(Node.pool_id == pool_id).limit(15).all())
    form = ObjectForm(obj)
    print app.instance_path
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'photos', filename
        ))
        return redirect(url_for('pool'))
    # print user_data
    # print pool_data
    # for node in node_data:
    #     if node["is_on_pool"] == True:
    #         if pool_id == node["pool_id"]:
    #             print node
    return render_template('pool.html', data_table=post_data, form=form, title=pool_data.name, nodes=node_data)
    # if request.method == 'POST':
    #     data = json.loads(request.data)
    #     print user_id, data
    #     if not check_node(data["mac"]):
    #         n = Node(name=data["name"], user_id=user_id, mac=data["mac"])
    #         db.session.add(n)
    #         db.session.commit()
    #         return 'node successfully added'
    #     else:
    #         return 'node already exist'


app.config["UPLOAD_FOLDER"] = "uploads"

@app.route('/pool/<pool_id>/attach/', methods=['POST'])
def attachNode(pool_id):
    attachForm = AttachNode()
    print 'data from attachNode',attachForm.data['nodes']
    node = Node.query.filter_by(id=attachForm.data['nodes']).first()
    node.pool_id = pool_id
    print 'data', node.pool_id
    db.session.add(node)
    db.session.commit()
    flash('Node was attached succesfully to the pool.', 'info')
    return redirect(url_for('pools'))


@app.route('/pool/<pool_id>/detach/', methods=['POST'])
def detachNode(pool_id):
    detachForm = DetachNode()
    print 'data from detachNode',detachForm.data['nodes']
    node = Node.query.filter_by(id=detachForm.data['nodes']).first()
    node.pool_id = None
    print 'data', node.pool_id
    db.session.add(node)
    db.session.commit()
    flash('Node was detached succesfully from the pool.', 'info')
    return redirect(url_for('pools'))


@app.route('/pools', methods=['GET', 'POST'])
def pools():
    attachForm = AttachNode()
    # print attachForm
    detachForm = DetachNode()
    count_nodes={}
    if request.method == 'GET':
        pool_data = data_to_json(Pool.query.all())
        for pool in pool_data:
            print pool['id']
            pool['count']=len(Node.query.filter_by(pool_id=pool['id']).all())
            print pool['count'], pool_data
        #### a call to count the numbers of nodes in the pool ###
        return render_template('pools.html', detachForm=detachForm, attachForm=attachForm,  title='List of pools available', pools=pool_data)


    # if request.method == 'POST':
    #     data = json.loads(request.data)
    #     print user_id, data
    #     if not check_node(data["mac"]):
    #         n = Node(name=data["name"], user_id=user_id, mac=data["mac"])
    #         db.session.add(n)
    #         db.session.commit()
    #         return 'node successfully added'
    #     else:
    #         return 'node already exist'


@app.route('/pools/<user_id>', methods=['GET', 'POST'])
def user_pools(user_id):
    if request.method == 'GET':
        # pool_data = UserPool.query.filter_by(user_id=user_id).first()
        user = User.query.filter_by(id=user_id).first()
        attachForm = AttachNode()
        print attachForm
        detachForm = DetachNode()
        return render_template('pools.html', detachForm=detachForm, attachForm=attachForm, title='List of pools available for {}'.format(user.username))
        # return render_template('pools.html', detachForm=detachForm, attachForm=attachForm, title='List of pools available for {}'.format(user.username), posts=pool_data)
    # if request.method == 'POST':
    #     data = json.loads(request.data)
    #     print user_id, data
    #     if not check_node(data["mac"]):
    #         n = Node(name=data["name"], user_id=user_id, mac=data["mac"])
    #         db.session.add(n)
    #         db.session.commit()
    #         return 'node successfully added'
    #     else:
    #         return 'node already exist'


@app.route('/qrcode', methods=['GET'])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get('data', '')
    return send_file(
        qrcode(data, mode='raw'),
        mimetype='image/png'
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('access/register.html', title='Register', form=form)



def modify_time_sort(file_name):
    file_path = "uploads/{}".format(file_name)
    file_stats = os.stat(file_path)
    last_access_time = file_stats.st_atime
    return last_access_time


@app.route("/filenames", methods=["GET"])
def get_filenames():
    filenames = os.listdir("uploads/")
    modify_time_sort = lambda f: os.stat("uploads/{}".format(f)).st_atime
    filenames = sorted(filenames, key=modify_time_sort)
    return_dict = dict(filenames=filenames)
    return jsonify(return_dict)


@app.route("/sendfile", methods=["POST"])
def send_file():
    fileob = request.files["file2upload"]
    filename = secure_filename(fileob.filename)
    save_path = "{}/{}".format(app.config["UPLOAD_FOLDER"], filename)
    fileob.save(save_path)
    return "successful_upload"


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = Object()
    print app.instance_path
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'photos', filename
        ))
        return f
        # return redirect(url_for('index'))
    return 'adsadsadsad'

    # return render_template('upload.html', form=form)

# @app.route('/upload', methods=['POST'])
# def upload():
#     file = request.files['input file']
#     file = QRcode(app)
#     new_file = Object(name=file.filename, data=file.read())
#     db.session.add(new_file)
#     db.session.commit()
#     return file.filename


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        data = data_to_json(User.query.limit(15).all())
        print jsonify(data)
        return render_template('users.html', title='List of nodes availables', nodes=data)
    if request.method == 'POST':
        user = User.query.filter_by(email=request.data)
        for i in user:
            user_id = i
        return jsonify(user_id.id)


@app.route('/user/<user_id>', methods=['GET', 'POST'])
@login_required
def user_profile(user_id):
    if request.method == 'GET':
        # node = data_to_json(Node.query.filter(Node.user_id == user_id).all())
        # for n in node:
        #     print n["id"]
        # # user = jsonify(node)
        # posts = data_to_json(Post.query.filter(Post.node_id == user).limit(15).all())
        data_nodes = data_to_json(Node.query.filter(Node.user_id == user_id).limit(15).all())
        data_pools = data_to_json(Pool.query.filter(Node.pool_id.isnot(None)).limit(15).all())
        profile = data_to_json(User.query.filter(User.id == user_id).all())
        return render_template('user.html', nodes=data_nodes, pools=data_pools, title='List of nodes availables',
                               user=user_id, user_profile=profile)
        return 'node successfully added'
    if request.method == 'POST':
        data = json.loads(request.data)
        if not check_node(data["mac"]):
            n = Node(name=data["name"], user_id=user_id, mac=data["mac"])
            db.session.add(n)
            db.session.commit()
            return 'node successfully added'
        else:
            return 'node already exist'


@app.route('/user/<user_id>/node/<node_id>', methods=['GET', 'POST'])
@login_required
def node_profile(user_id, node_id):
    if request.method == 'GET':
        node = Node.query.filter(Node.id == node_id)
        for i in node:
            node_data = i
        if not node:
            print 'No Node found.'
            return 'Error 404'
        data = data_to_json(Post.query.filter(Post.node_id == node_id).all())
        return render_template('node.html', title=node_data.name, data_table=data)
    if request.method == 'POST':

        print 'hacer algo'
        return 'todo...'


# @app.route('/user/<user_id>/upload', methods=['GET', 'POST'])
# def upload_file(user_id):
#     if request.method == 'POST':
#         file = request.files['file']
#         User.query().filter_by(id=user_id).update(profile_image=file.read())
#
#         app.db.session.commit()
#     return '''
#         <!doctype html>
#         <title>Upload new File</title>
#         <h1>Upload new File</h1>
#         <form action="" method=post enctype=multipart/form-data>
#           <p><input type=file name=file>
#              <input type=submit value=Upload>
#         </form>
#         '''
#     # if request.method == 'POST':
#     #     # check if the post request has the file part
#     #     if 'file' not in request.files:
#     #         flash('No file part')
#     #         return redirect(request.url)
#     #     file = request.files['file']
#     #     # if user does not select file, browser also
#     #     # submit a empty part without filename
#     #     if file.filename == '':
#     #         flash('No selected file')
#     #         return redirect(request.url)
#     #     if file and allowed_file(file.filename):
#     #         filename = secure_filename(file.filename)
#     #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#     #         return redirect(url_for('upload_file',
#     #                                 filename=filename))
#     # return '''
#     # <!doctype html>
#     # <title>Upload new File</title>
#     # <h1>Upload new File</h1>
#     # <form action="" method=post enctype=multipart/form-data>
#     #   <p><input type=file name=file>
#     #      <input type=submit value=Upload>
#     # </form>
#     # '''