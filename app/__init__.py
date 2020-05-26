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
    get_jwt_identity,jwt_refresh_token_required,get_raw_jwt
)

file = UploadSet('file')
db = SQLAlchemy()
jwt = JWTManager()
blacklist = set()


# For this example, we are just checking if the tokens jti
# (unique identifier) is in the blacklist set. This could
# be made more complex, for example storing all tokens
# into the blacklist with a revoked status when created,
# and returning the revoked status in this call. This
# would allow you to have a list of all created tokens,
# and to consider tokens that aren't in the blacklist
# (aka tokens you didn't create) as revoked. These are
# just two options, and this can be tailored to whatever
# your application needs.


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    # return jti in blacklist
    if jti in blacklist:
        return False
    else:
        return True

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