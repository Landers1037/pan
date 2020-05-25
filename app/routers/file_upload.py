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
from sqlalchemy.exc import OperationalError

@api.route('/api/upload',methods=['POST'])
@jwt_required
def upload():
    if request.files:
        try:
            file_name = request.files['file'].filename
            file.save(request.files['file'],name=file_name)
            try:
                f = File(name=file_name)
                db.session.add(f)
                db.session.commit()
            except OperationalError:
                db.create_all()
                f = File(name=file_name)
                db.session.add(f)
                db.session.commit()
            return http_response(200,'ok','file uploaded')

        except UploadNotAllowed:
            http_response(250, 'bad', 'file ext not allowed')

    return http_response(250, 'bad', 'file upload filed')