#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# 根据一个 path, 创建不同命 文件夹;
# eg: usr/demo
# 存在   ==> 创建 usr/demo 1
# 不存在 ==> 创建 usr/demo
def creat_dir(dir_path, index):
    dir_out = dir_path
    if os.path.isdir(dir_path):
        dir_out = dir_out + " {}".format(index)
        if os.path.isdir(dir_out):
            dir_out = creat_dir(dir_path, index + 1)
        else:
            os.mkdir(dir_out)
    else:
        os.mkdir(dir_out)
    return dir_out

