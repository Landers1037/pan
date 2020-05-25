# -*- coding: utf-8 -*-
# Time: 2020-05-23 17:47
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: file.py

from app import db
import time

class File(db.Model):
    __tablename__ = 'file'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    time = db.Column(db.String(100))

    def __init__(self,name):
        self.name = name
        self.time = time.strftime('%Y-%m-%d',time.localtime())

    def info(self):
        return {
            "id": self.id,
            "name": self.name,
            "time": self.time
        }