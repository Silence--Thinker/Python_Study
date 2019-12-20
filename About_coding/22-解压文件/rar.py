#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from unrar import rarfile
import sys
sys.path.append(r"./")
import creatDir as CreatDir

def un_rar(file_path):
    """ unrar file """
    file_basename = os.path.basename(file_path)
    dir_path = os.path.splitext(file_path)[0]
    # outFile = CreatDir.creat_dir(dir_path, 1)
    outFile = "/Users/silence/Desktop/Temp/test/test/"
    file_list = []
    index = 0

    with rarfile.RarFile(file_path, 'r') as rar:
        file_name_list = rar.namelist()
        file_list = list(file_name_list)
        # os.chdir(outFile)
        # rar.extractall()
        # rar.close()
        # return
        # 需要密码
        if rar.needs_password():
            file_list = list(file_name_list)
            os.chdir(outFile)
            rar.extractall()
            pass
        # 不需要密码
        else:
            for file_name in file_name_list:
                index += 1
                file_list.append(file_name)
                print "==== {}".format(file_name)
                rar.extract(file_name, './')
    # os.chdir(outFile)
    # rar.extractall()
    # rarFile.close()
    print "已解压文件 {} 中: {}个文件, 目标文件夹为: {}".format(file_basename, len(file_list), os.path.basename(outFile))

un_rar("/Users/silence/Desktop/Temp/test/Archive.rar")

