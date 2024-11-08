from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def myapp():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"  # 未登录时

    # 注册蓝图
    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/')

    return app


from app.models import User  # 延时导入


# 在LoginManager 加载用户
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
