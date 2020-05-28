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
    hex = db.Column(db.String(100),nullable=False)
    time = db.Column(db.String(100))
    category = db.Column(db.String(50),default='default')


    def __init__(self,name,hex,category):
        self.name = name
        self.hex = hex
        self.time = time.strftime('%Y-%m-%d',time.localtime())
        self.category = category

    def info(self):
        return {
            "id": self.id,
            "name": self.name,
            "hex": self.hex,
            "time": self.time,
            "category": self.category
        }