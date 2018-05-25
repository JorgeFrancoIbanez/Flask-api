from app.models import Node, User
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import BooleanField, FileField, PasswordField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class DetachNode(FlaskForm):
    nodes = SelectField()

    def __init__(self):
        super(DetachNode, self).__init__()
        self.nodes.choices = [(g.id, g.name) for g in Node.query.filter(Node.pool_id.isnot(None),
                                                                        Node.user_id == current_user.id).order_by('name')]


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class ObjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    qrcode = FileField(validators=[FileRequired()])
    submit = SubmitField('Add object')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')