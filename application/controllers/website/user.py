# -*- coding: utf-8 -*-
from uuid import uuid4
import os
from flask import (Blueprint, current_app, request, flash, jsonify, Response,
        url_for, redirect, session, abort, render_template, make_response)
from flask_login import login_user, current_user, logout_user, \
        confirm_login, login_fresh, fresh_login_required, login_required
from configs.config import TEMPLATE_DIR
import application.models as Models


user = Blueprint('usercenter', __name__, url_prefix='/api/usercenter')

@user.route('/getUserInfo', methods=["GET",'POST'])
def get_user_info():
    data = request.args
    openId = data.get('openId')
    sign = data.get('sign')
    time = data.get('time')
    return jsonify(message='OK')