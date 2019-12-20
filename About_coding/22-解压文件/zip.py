#!/usr/bin/python
# -*- coding: utf-8 -*-

import zipfile
import os
import sys
sys.path.append(r"./")
# from creatDir import creat_dir
import creatDir as CreatDir

# .zip 文件的解压方式
def un_zip(file_path):
    """unzip zip file"""
    file_basename = os.path.basename(file_path)
    dir_path = os.path.splitext(file_path)[0]
    outFile = CreatDir.creat_dir(dir_path, 1)

    file_list = []
    index = 0
    zip_file = zipfile.ZipFile(file_path, "r")
    for fileInfo in zip_file.infolist():
        if fileInfo.filename.startswith("__MACOSX"):
            pass
        else:
            index += 1
            file_list.append(fileInfo.filename)

            # 是加密文件
            if fileInfo.flag_bits & 0x01:
                zip_file.extract(fileInfo.filename, outFile, '1234')
                pass
            # 不是加密文件
            else:
                zip_file.extract(fileInfo.filename, outFile)
    zip_file.close()
    print "已解压文件 {} 中: {}个文件, 目标文件夹为: {}".format(file_basename, len(file_list), os.path.basename(outFile))


un_zip("/Users/silence/Desktop/Temp/test/demo.zip")

# dir_path = "/Users/silence/Desktop/Temp/test/demo"
# creat_dir(dir_path, 1)
