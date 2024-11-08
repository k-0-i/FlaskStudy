from flask import render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user

from app import db
from app.auth import auth_bp
from app.auth.forms import LoginForm, RegisterForm
from app.models import User


#
@auth_bp.route('/')
def index():
    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    注册界面
    :return:
    """
    error_message = None
    form = RegisterForm()
    if form.validate_on_submit():
        # 密码加密
        # hashed_password = generate_password_hash(form.password.data)
        # user = User(username=form.username.data, password_hash=hashed_password)
        #     添加到数据库
        #     db.session.add(user)
        #     db.session.commit()
        is_exist = User.query.filter_by(username=form.username.data).first()
        if is_exist:
            error_message = "用户名已经存在，请更换一个不同的用户名"
        else:
            # 如果用户名不存在，则创建一个新用户，并重定向到登陆界面
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title="Regisiter",form=form,error_message=error_message)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    登陆界面
    :return:
    """
    form = LoginForm()
    error_message = None
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            # flash('登陆成功，欢迎用户 {}，Remember—Me {}'.format(
            #     form.username.data, form.remember_me.data
            # ), 'success')
            return redirect(url_for('dashboard.dashboard'))
        else:
            # flash('用户名或密码错误','failed')
            error_message = "用户名或密码错误"

    # return render_template('auth/login.html', title="Sign In", form=form)
    return render_template('auth/login.html', title="Sign In", form=form, error_message=error_message)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
