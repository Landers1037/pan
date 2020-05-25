# -*- coding: utf-8 -*-
# Time: 2020-05-23 11:53
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: http_response.py

from flask import jsonify
from flask import abort

def http_response(code: int,msg: str,data):
    if code == 401:
        return abort(401)
    elif code == 500:
        return abort(500)
    else:
        return jsonify({
            "code": code,
            "msg": msg,
            "data": data
        })