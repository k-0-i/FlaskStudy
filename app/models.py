from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'  # 如果不指定，默认表名为类名小写，User => user  UserName => user_name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    # email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(256))

    def __init__(self, username):
        """
        初始化
        :param username:
        """
        self.username = username

    def set_password(self, password):
        """
        设置密码
        :return: 无返回值
        """
        self.password_hash = generate_password_hash(password=password)

    def check_password(self, password):
        """
        检查密码是否正确
        :param password:
        :return:
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
