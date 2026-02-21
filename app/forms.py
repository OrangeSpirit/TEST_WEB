from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('FIO', validators=[DataRequired(), Length(min=2, max=100)])
    login = StringField('login', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('submit password', validators=[DataRequired(), EqualTo('password')])
    avatar = FileField('upload avatar', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('registration')
