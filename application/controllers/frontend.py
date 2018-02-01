# -*- coding: utf-8 -*-

from uuid import uuid4
import os
from flask import (Blueprint, current_app, request, flash, jsonify, Response,
        url_for, redirect, session, abort, render_template, make_response)
from flask_login import login_user, current_user, logout_user, \
        confirm_login, login_fresh, fresh_login_required, login_required
from configs.config import TEMPLATE_DIR
import application.models as Models
from datetime import datetime,timedelta


frontend = Blueprint('frontend', __name__, url_prefix='')


def redirect_next():
    return redirect(url_for('admin.index'))

@frontend.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@frontend.route('/admin/login', methods=['GET', 'POST'])
def login():
    if request.user_agent.platform in ['ipad', 'iphone', 'android']:
        return jsonify(error=u"请先登录")
    if current_user.is_authenticated:
        return redirect_next()
    if request.method == 'POST':
        email = request.form.get('email', None)
        password = request.form.get('password', None)
        if email and password:
            user, authenticated = Models.SystemUser.authenticate(email=email, password=password)
        else:
            flash("请输入正确的用户名和密码")
            return redirect_next()
        if user and authenticated:
            remember = True
            login_user(user, remember)
        else:
            flash(u'账号或密码不正确')

        return redirect_next()

    return render_template('admin/user/login.html')



@frontend.route('/admin/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('frontend.login'))
