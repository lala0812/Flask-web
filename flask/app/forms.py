from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from app.models import User

class RegisterForm(FlaskForm):
    #使用valodators對資料限制格式
    username = StringField('Username',  validators=[DataRequired(), Length(min=4, max=20)])
    email  = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=4, max =20)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    # recaptchar = RecaptchaField() #我不是機器人
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("Username already taken")
        
class LoginForm(FlaskForm):
    username = StringField('Username',  validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=4, max =20)])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign in')

class PostTweetForm(FlaskForm):
    text = TextAreaField('Say something ...', validators=[DataRequired(), Length(max=140, min=1)])
    submit = SubmitField('Post')