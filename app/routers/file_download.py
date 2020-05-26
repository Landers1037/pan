# -*- coding: utf-8 -*-
# Time: 2020-05-26 17:48
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: file_download.py

#文件权限的校验
from flask import request,make_response
from app import jwt_required
from . import api
from app.models import File

@api.route('/download')
@jwt_required
def donwload():
    """
    for nginx download with token access
    choose to use origin name or secure name
    :return:
    """
    filename = request.args.get('file')
    origin_name = get_orgin_name(filename)

    res = make_response('send file')
    res.headers['Content-Disposition'] = 'attachment;filename={}'.format(filename)
    res.headers['Content-Type'] = 'application/octet-stream;charset=utf-8'
    res.headers['X-Accel-Redirect'] = '/file/{}'.format(filename)

    return res

def get_orgin_name(filename):
    f = File.query.filter_by(hex=filename).first()
    if f:
        return f.name
    return filename