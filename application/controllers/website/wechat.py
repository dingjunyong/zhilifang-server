# -*- coding: utf-8 -*-
from uuid import uuid4
import os
from flask import (Blueprint, current_app, request, flash, jsonify, Response,
        url_for, redirect, session, abort, render_template, make_response)
from flask_login import login_user, current_user, logout_user, \
        confirm_login, login_fresh, fresh_login_required, login_required
from configs.config import TEMPLATE_DIR
import application.models as Models
from weixin import WXAPPAPI


wechat = Blueprint('wechat', __name__, url_prefix='/api/wechat')

@wechat.route('/jscode2session', methods=['GET','POST'])
def jscode2session():
    api = WXAPPAPI(appid="wxfb39705a144d0144",
                   app_secret="e8cd29ee68a6131d3bb7fdd98b5022f4")
    data = request.args
    code = data.get('jsCode')
    nickNmae = data.get('nickNmae')
    session_info = api.exchange_code_for_session_key(code=code)
    session_info['expires_in']='7200'
    openid=session_info.get("openid")
    user=Models.User.filter_by(wx_openid=openid).first()
    if not user:
        Models.User.create(openid,nickNmae)
    return  jsonify({"result":True,"data":session_info})


@wechat.route('/user2session', methods=['GET','POST'])
def user2session():
    return  jsonify(message='OK')


