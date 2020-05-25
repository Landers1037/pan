# -*- coding: utf-8 -*-
# Time: 2020-05-23 17:57
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: db_init.py

#数据库初始化
from app import db
from . import api
from app.response import http_response

@api.route('/api/db_init',methods=['POST'])
def db_init():
    db.create_all()
    return http_response(200,'ok','database init')