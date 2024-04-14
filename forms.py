from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()], render_kw={"size": "30"})
    password = PasswordField(label='Password', validators=[DataRequired()], render_kw={"size": "30"})
    submit = SubmitField('Login')
