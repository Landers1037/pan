# -*- coding: utf-8 -*-
# Time: 2020-05-23 16:21
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: file_upload.py

from app.response import  http_response
from . import api
from app import file
from flask import request
from app.custom.flask_uploads import UploadNotAllowed
from app.models import File
from app import db,jwt_required
from app.utils import secure_name
from sqlalchemy.exc import OperationalError

@api.route('/api/upload',methods=['POST'])
@jwt_required
def upload():
    """
    upload file and save file in local disk.
    http-request's form should have [file] part
    :return:
    """
    if request.files:
        try:
            file_name = request.files['file'].filename
            #无需考虑文件名重复的问题
            hex = secure_name(file_name)
            file.save(request.files['file'],name=hex)
            try:
                f = File(name=file_name,hex=hex)
                db.session.add(f)
                db.session.commit()

            except OperationalError:
                db.session.rollback()
                return http_response(250, 'bad', 'database not exist')

            return http_response(200,'ok','file uploaded')


        except UploadNotAllowed:
            http_response(250, 'bad', 'file ext not allowed')

    return http_response(250, 'bad', 'file upload filed')

