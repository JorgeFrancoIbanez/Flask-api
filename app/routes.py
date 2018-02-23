
from app import app
from app.forms import LoginForm
from flask import flash, jsonify, redirect, render_template, request, url_for
from app.utils.convert_json import data_to_json
from app.models import Post, Node


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jorge'}
    title = 'Cam application'
    return render_template('index.html', title=title, user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/monitor-test')
def cams():
    posts = Post.query.limit(15).all()
    data = data_to_json(posts)
    return render_template('table.html', title='Camera monitoring system', data_table=data)


@app.route('/refresh', methods=['GET'])
def stuff():
    posts = Post.query.limit(15).all()
    data = data_to_json(posts)
    print jsonify(data)
    return render_template('table.html', data_table=data)


@app.route('/noderefresh', methods=['GET'])
def node_refresh():
    if request.method == 'GET':
        id = request.url[:0]
        print 'get', id
        data = data_to_json(Post.query.filter(Post.node_id == id).all())
        return render_template('node.html', data_table=data)


@app.route('/nodes')
def nodes():
    data = data_to_json(Node.query.limit(15).all())
    print jsonify(data)
    return render_template('nodes.html', title='List of nodes availables', nodes=data)


@app.route('/node/<id>', methods=['GET', 'POST'])
def node(id):
    if request.method == 'GET':
        node = Node.query.filter(Node.id == id)
        for i in node:
            node_data = i
        if not node:
            print 'No Node found.'
            return 'Error 404'
        data = data_to_json(Post.query.filter(Post.node_id == id).all())
        return render_template('node.html', title=node_data.name, data_table=data)
    if request.method == 'POST':

        print 'hacer algo'
        return 'todo...'

