'''from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    login = StringField('login', validators=[DataRequired()])
    password = StringField('password', validator=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
'''