# -*- coding: utf-8 -*-
# Time: 2020-05-23 18:00
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: file_list.py

from . import api
from app.models import File
from app.response import http_response
from app import jwt_required
from flask import request


@api.route('/api/file_list')
@jwt_required
def file_list():
    """
    return all file list
    :return:
    """
    cate = request.args.get('cate')
    if cate == 'all' or not cate:
        try:
            fl = File.query.all()
            flist = [f.info() for f in fl]
            return http_response(200,'ok',flist)

        except Exception as e:
            print(e.args)
            return http_response(250,'bad','get file_list failed')
    else:
        try:
            fl = File.query.filter_by(category=cate).all()
            flist = [f.info() for f in fl]
            return http_response(200, 'ok', flist)

        except Exception:
            return http_response(250, 'bad', 'get file_list failed')