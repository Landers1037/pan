# -*- coding: utf-8 -*-
# Time: 2020-05-23 11:16
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: normal_config.py

import os

class Normal_Config:
    DEBUG = True
    SECRET_KEY = 'this_is_a_secret_key'
    #nginx
    FILE_ACCESS = True
    FILE_SERVER_URI = 'http://localhost:5000'
    FILE_PATH = '/file/'
    #file
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024 * 1024
    UPLOADED_FILE_DEST = os.path.join(os.getcwd(),'upload_file')
    UPLOADED_FILE_URL = FILE_SERVER_URI + FILE_PATH
    UPLOADED_FILE_ALLOW = '*'
    UPLOADED_FILE_DENY = ('bat', 'sh','db','sqlite','sql','bash','o')
    UPLOADS_DEFAULT_DEST = os.path.join(os.getcwd(),'upload_file')
    UPLOADS_DEFAULT_URL = FILE_SERVER_URI + FILE_PATH
    #sql
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.getcwd()+"/pan.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    #jwt
    JWT_TOKEN_LOCATION = 'query_string'
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    JWT_QUERY_STRING_NAME = 'token'
    JWT_BLACKLIST_ENABLED = True