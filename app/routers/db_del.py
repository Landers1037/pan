# -*- coding: utf-8 -*-
# Time: 2020-05-23 17:58
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: db_del.py

#清空表结构

from . import api
from app import db
from app.response import http_response

@api.route('/api/db_del',methods=['POST'])
def db_del():
    db.drop_all()
    return http_response(200,'ok','database deleted')