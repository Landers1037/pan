# -*- coding: utf-8 -*-
# Time: 2020-05-26 13:08
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: logout.py

from . import  api
from app.response import http_response
from app.models import User
from app import db
from flask import request
from app import get_jwt_identity,jwt_required,get_raw_jwt,blacklist


@api.route('/api/logout',methods=['DELETE'])
@jwt_required
def logout():
    try:
        # current_user = get_jwt_identity()
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)

    except:
        return http_response(250, 'bad', 'user logout failed')

    return http_response(460,'ok','user logout, thanks for using pan')
