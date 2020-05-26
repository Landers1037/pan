# -*- coding: utf-8 -*-
# Time: 2020-05-23 11:19
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: user_auth.py

from . import  api
from app.response import http_response
from app.models import User
from app import db
from flask import request

@api.route('/api/sign_up',methods=['post'])
def sign_up():
    if request.json:
        try:
            #添加用户的去重
            name = request.json.get('name','test')
            password = request.json.get('password','123456')
            get_user = User.query.filter_by(name=name).first()
            if get_user:
                return  http_response(250, 'bad', 'user already exist')
            try:
                u = User(name=name,password=password)
                db.session.add(u)
                db.session.commit()
            except:
                db.session.rollback()
                return http_response(250, 'bad', 'user added failed')
            # pass
        except:
            return http_response(250, 'bad', 'user added failed')

        return http_response(200,'ok','user added success')

    else:
        return http_response(250, 'bad', 'json data required')