# -*- coding: utf-8 -*-
# Time: 2020-05-23 18:06
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: file_name.py


from . import api
from app.models import File
from app.response import http_response
from flask import request,current_app
from app import file,jwt_required

@api.route('/api/file_info')
@jwt_required
def file_info():
    """
    get one file's info which contains [name,hex_name,url]
    when FILE_ACCESS is True, url is generated by FILE_SERVER_URI
    it's a sample about nginx server, see file_download for more
    :return:
    """
    try:
        name = request.args.get('name')
        f = File.query.filter_by(hex=name).first()
        if f:
            url = file.url(f.hex) if not current_app.config["FILE_ACCESS"] \
                else current_app.config["FILE_SERVER_URI"] +'/download?file=' + f.hex

            fdict = {
                "name": f.name,
                "time": f.time,
                "hex": f.hex,
                "url": url,
                "category": f.category
            }
            return http_response(200,'ok',fdict)
        else:
            return http_response(250, 'bad', 'file not exists')

    except Exception as e:
        print(e.args)
        return http_response(250,'bad','get file info failed')