# -*- coding: utf-8 -*-
# Time: 2020-05-28 10:02
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: auto_category.py

def auto_category(name):
    """
    this function helps to choose a category of file automatically
    :param name:
    :return:
    """
    name = name.lower()
    DOCUMENT = ('pdf','doc','docx','ppt','pptx','xls','xlsx','csv','mobi','epub','azw3','txt')
    ARCHIVE = ('zip','bz2','gzip','tar','gz','7z','rar')
    MEDIA = ('mp4','gif','jpg','jpeg','png','webp','webm','mov','rmvb','mkv','mp3','flac')
    EXE = ('sh','exe','dmg','app','appimage','msi','java','js','py','go','html','css','bat')

    if len(name.split('.')) <= 1:
        return 'default'
    else:
        ext = name.split('.')[-1]
        if ext in DOCUMENT:
            return 'document'

        elif ext in ARCHIVE:
            return 'archive'

        elif ext in MEDIA:
            return 'media'

        elif ext in EXE:
            return 'exe/code'

        else:
            return 'default'
