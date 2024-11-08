from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    """
    继承、重写FlaskForm
    """
    username = StringField('Username', validators=[DataRequired()])  # 值 必需
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=4, max=20, message="用户名长度范围4~20")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=6, message='密码长度不少六位'),
        # EqualTo('confirm_password', message='密码必须匹配'),
    ])
    confirm_password = PasswordField('Confire Password', validators=[
        DataRequired(),
        EqualTo('password', message='密码必须匹配')
    ])
    submit = SubmitField('Register')

    # def validate_username(self, username):
    #     """
    #     验证用户名是否已经存在
    #     :param username:
    #     :return:
    #     """
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationErr('用户名已经存在，请换一个不同的用户名')
