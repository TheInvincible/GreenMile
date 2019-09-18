from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, ValidationError, BooleanField, SubmitField
from wtforms.widgets import CheckboxInput
from wtforms.validators import DataRequired, Email, EqualTo, Length

from ...models import User

class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = CheckboxInput('Remember Me')
    submit = SubmitField('Login')
