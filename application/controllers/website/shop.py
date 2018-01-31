# -*- coding: utf-8 -*-
from uuid import uuid4
import os
from flask import (Blueprint, current_app, request, flash, jsonify, Response,
        url_for, redirect, session, abort, render_template, make_response)
from flask_login import login_user, current_user, logout_user, \
        confirm_login, login_fresh, fresh_login_required, login_required
from configs.config import TEMPLATE_DIR
import application.models as Models


shop = Blueprint('shop', __name__, url_prefix='/api/shops')

@shop.route('/register', methods=['POST'])
def register():
    data = request.form
    shop_name = data.get('shop_name')
    mobile_number = data.get('mobile_number')
    mobile_code = data.get('mobile_code')
    password = data.get('password')
    if not shop_name or not mobile_number or not mobile_code or not password:
        return jsonify(message='Failed', error='输入参数有误')
    user = Models.User.query.filter_by(mobile_number=mobile_number).first()
    if user:
        return jsonify(message='Failed', error='手机号码已被注册！')
    #注册店铺
    shop =  Models.Shop.create(shop_name)
    Models.ShopMember.create(mobile_number,True,shop.id)
    return jsonify(message='OK')