# -*- coding: utf-8 -*-
# Time: 2020-05-26 11:36
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: cancel_account.py

from . import  api
from app.response import http_response
from app.models import User
from app import db
from flask import request
from app import get_jwt_identity,jwt_required,get_raw_jwt,blacklist


@api.route('/api/cancel_account',methods=['DELETE'])
@jwt_required
def cancel_account():
    """
    user can cancel their account, if get this api their token will be added into blacklist.
    once token has been added into blacklist, user's account will be deleted from database
    :return:
    """
    if request.json:
        try:
            #添加用户的去重
            name = request.json.get('name',None)
            get_user = User.query.filter_by(name=name).first()
            if not get_user:
                return  http_response(250, 'bad', 'user not exist')
            try:
                current_user = get_jwt_identity()
                if current_user == get_user.name:
                    try:
                        db.session.delete(get_user)
                        db.session.commit()
                    except:
                        db.session.rollback()
                    jti = get_raw_jwt()['jti']
                    blacklist.add(jti)

            except Exception:
                return http_response(250, 'bad', 'user cancel failed')
            # pass
        except Exception as e:
            print(e.args)
            return http_response(250, 'bad', 'user cancel failed')

        return http_response(460,'ok','user canceled, thanks for using pan')

    else:
        return http_response(250, 'bad', 'json data required')