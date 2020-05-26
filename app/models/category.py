# -*- coding: utf-8 -*-
# Time: 2020-05-25 22:31
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: category.py

from app import db


class Cat(db.Model):
    __tablename__ = 'cat'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category = db.Column(db.String(50), nullable=False)

    def __init__(self, category):
        self.category = category

    def info(self):
        return {
            "category": self.category
        }