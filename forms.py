from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired()], render_kw={"size": "30"})
    password = StringField('Password', [DataRequired()], render_kw={"size": "30"})
