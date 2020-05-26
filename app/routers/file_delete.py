# -*- coding: utf-8 -*-
# Time: 2020-05-24 10:42
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: file_delete.py

from . import api
from app.models import File
from app import db
from app.response import http_response
from app import file,jwt_required
from flask import request
import os

@api.route('/api/file_delete',methods=['POST'])
@jwt_required
def file_delete():
    """
    delete file by it's hex name
    if exists, also remove from disk
    :return:
    """
    if request.json:
        try:
            name = request.json['name']
            f = File.query.filter_by(hex=name).first()
            if f:
                try:
                    path = file.path(f.hex)
                    os.remove(path)
                    db.session.delete(f)
                    db.session.commit()
                except:
                    db.session.rollback()
                    return http_response(250, 'bad', 'file delete filed')

                return http_response(200,'ok','file deleted')
            else:
                return http_response(250, 'bad', 'file not exists')

        except Exception as e:
            print(e.args)
            return http_response(250,'bad','get file info failed')
    else:
        return http_response(250, 'bad', 'json data required')