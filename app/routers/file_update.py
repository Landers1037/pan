# -*- coding: utf-8 -*-
# Time: 2020-05-26 22:00
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: file_update.py

from . import api
from app.models import File
from app.response import http_response
from flask import request
from app import jwt_required,db

@api.route('/api/file_update',methods=['POST'])
@jwt_required
def file_update():
    """
    update file's name, hex name is unique but name(origin name) can be same
    :return:
    """
    if request.json:
        try:
            hex_name = request.json.get('hex_name')
            name = request.json.get('name')
            f = File.query.filter_by(hex=hex_name).first()
            if f and name:
                f.name = name
                db.session.commit()
                return http_response(200,'ok','file info updated')
            else:
                return http_response(250, 'bad', 'file not exists')

        except:
            return http_response(250,'bad','update file info failed')
    else:
        return http_response(250,'bad','json data required')