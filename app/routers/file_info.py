# -*- coding: utf-8 -*-
# Time: 2020-05-23 18:06
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: file_name.py


from . import api
from app.models import File
from app.response import http_response
from flask import request
from app import file,jwt_required

@api.route('/api/file_info')
@jwt_required
def file_info():
    try:
        name = request.args.get('name')
        f = File.query.filter_by(name=name).first()
        if f:
            fdict = {
                "name": f.name,
                "time": f.time,
                "url": file.url(f.name)
            }
            return http_response(200,'ok',fdict)
        else:
            return http_response(250, 'bad', 'file not exists')

    except Exception as e:
        print(e.args)
        return http_response(250,'bad','get file info failed')