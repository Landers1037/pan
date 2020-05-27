# -*- coding: utf-8 -*-
# Time: 2020-05-26 20:45
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: secure_name.py

import uuid
import time

def secure_name(file_name):
    file_name = file_name if file_name else 'none.ext'
    time_now = str(time.time())
    if len(file_name.split('.')) <= 1:
        ext = ''
    else:
        ext = '.' + file_name.split('.')[-1]
    return uuid.uuid5(uuid.NAMESPACE_OID,file_name + time_now).hex + ext