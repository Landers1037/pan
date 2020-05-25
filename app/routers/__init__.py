# -*- coding: utf-8 -*-
# Time: 2020-05-23 11:18
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py

from flask.blueprints import Blueprint
from flask_cors import CORS

api = Blueprint('api',__name__)
CORS(api)

from . import file_upload
from . import file_list
from . import file_info
from . import file_delete
from . import search

from . import db_init
from . import db_del

from . import login
from . import sign_up