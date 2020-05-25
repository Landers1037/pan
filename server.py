# -*- coding: utf-8 -*-
# Time: 2020-05-22 20:47
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: server.py

from  app import create_app

app = create_app()

if __name__ == '__main__':

    app.run()