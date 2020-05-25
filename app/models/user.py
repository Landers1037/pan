# -*- coding: utf-8 -*-
# Time: 2020-05-23 20:23
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: user.py

from app import db

class User(db.Model):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50),nullable=False)