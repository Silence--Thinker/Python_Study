#!/usr/bin/python
# -*- coding: utf-8 -*-

import zipfile
import os

# .zip 文件的解压方式
def un_zip(file_path):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_path, "r")
    file_basename = os.path.basename(file_path)
    file_name = os.path.splitext(file_basename)[0]
    outfile = file_name
    if os.path.isdir(outfile):
        pass
    else:
        os.mkdir(outfile)
    file_list = []
    index = 0
    for i in zip_file.infolist():
        index += 1
        if i.flag_bits & 0x01:
            print "是加密文件"
        else:
            print "不是加密文件", index, i.filename
    for names in zip_file.namelist():
        if names.startswith("__MACOSX"):
            pass
        else:
            # index += 1
            file_list.append(names)
            # print "index {}, file name: {}".format(index, names)
            # zip_file.extract(names, outfile", "1122")
    zip_file.close()
    print "file count: {}".format(len(file_list))


un_zip("/Users/silence/Documents/GitHub/Python_Study/About_coding/22-解压文件/pic.zip")