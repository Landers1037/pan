# -*- coding: utf-8 -*-
# Time: 2020-05-26 20:45
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: secure_name.py

import uuid

def secure_name(file_name):
    file_name = file_name if file_name else 'none.ext'
    if len(file_name.split('.')) <= 1:
        ext = ''
    else:
        ext = '.' + file_name.split('.')[-1]
    return uuid.uuid5(uuid.NAMESPACE_DNS,file_name).hex + ext