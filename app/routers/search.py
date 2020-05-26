# -*- coding: utf-8 -*-
# Time: 2020-05-25 20:35
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: search.py


from . import api
from app.models import File
from app.response import http_response
from app import jwt_required
from flask import request

@api.route('/api/search')
@jwt_required
def file_search():
    """
    search file in database
    :return:
    """
    try:
        word = request.args.get('word')
        fl = File.query.filter(File.name.contains(word)).all()
        if fl:
            flist = [f.info() for f in fl]
            return http_response(200,'ok',flist)

        return http_response(250,'bad','empty search results')

    except Exception as e:
        print(e.args)
        return http_response(250,'bad','get file-list failed')