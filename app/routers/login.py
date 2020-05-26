# -*- coding: utf-8 -*-
# Time: 2020-05-23 20:34
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: login.py

from app.models import User
from app import create_access_token
from flask import request
from app.response import  http_response
from . import api

@api.route('/api/login',methods=['POST'])
def login():
    if request.json:
        name = request.json.get('name',None)
        password = request.json.get('password',None)
        try:
            u = User.query.filter_by(name=name).first()
            if u and u.password == password:
                token = create_access_token(identity=name)
                return http_response(200,'ok',token)
            else:
                return http_response(250,'bad','user illegal')
        except:
            return http_response(500,'bad','login failed')

    return http_response(250,'bad','json data required')

