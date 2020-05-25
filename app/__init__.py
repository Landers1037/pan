# -*- coding: utf-8 -*-
# Time: 2020-05-23 10:47
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py

from flask import Flask
from app.config.normal_config import Normal_Config
from app.custom.flask_uploads import UploadSet,configure_uploads
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

file = UploadSet('file')
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Normal_Config)
    #初始化文件set
    configure_uploads(app,file)
    db.init_app(app)
    jwt.init_app(app)

    from app.routers import api
    app.register_blueprint(api)

    return app