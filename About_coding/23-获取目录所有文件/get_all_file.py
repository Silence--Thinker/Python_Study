#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import re

def get_all_file(dirPath, match):
    file_path_list = []
    regexObj = re.compile(r'{}'.format(match))
    if os.path.exists(dirPath):
        pass
    else:
        return file_path_list
    if os.path.isdir(dirPath):
        child_file_list = os.listdir(dirPath)
        for file in child_file_list:
            file_path = dirPath + '/' + file
            if os.path.isdir(file_path):
                file_path_list = file_path_list + get_all_file(file_path, match)
            elif os.path.exists(file_path) and regexObj.search(file_path):
                file_path_list.append(file_path)
            else:
                pass
    return file_path_list

def find_unuse_image_in_tsx_file (dirPath):
    image_file_list = get_all_file(dirPath, '.png$|.jpg$')
    code_file_list = get_all_file(dirPath, '.tsx$|.js$|.jsx$|.ts$')
    print "匹配到的图片文件个数为: {}个".format(len(image_file_list))
    print "匹配到的code文件个数为: {}个".format(len(code_file_list))
    # for file in image_file_list:
        # print "=== {}".format(os.path.basename(file))
    image_file_unuse_list = list(image_file_list)

    for code_file in code_file_list:
        # print "=={}".format(code_file)
        with open(code_file, "r") as codeFile:
            line = codeFile.readline()
            lineCount = 1
            while line:
                for imageFile in image_file_list:
                    fileName = os.path.basename(imageFile)
                    if re.search(r'{}'.format(fileName.replace("@2x", "")), line, re.X):
                    #   re.search(r'{}'.format(fileName.replace("@2x", "")), line, re.X) or \
                    #   re.search(r'{}'.format(fileName.replace("@3x", "")), line, re.X):
                        # print "图片在{}文件{}行被用到了".format(fileName, lineCount)
                        if imageFile in image_file_unuse_list:
                            image_file_unuse_list.remove(imageFile)
                lineCount += 1
                line = codeFile.readline()

    print "未用到的图片个数为:{}".format(len(image_file_unuse_list))
    for unuse_file in image_file_unuse_list:
        fileName = os.path.basename(unuse_file)
        print "未用到的图片为: {}".format(fileName)

dirPath = "/Users/silence/Desktop/Working/flashbuy_mrn/src/pages"
child_file_list = os.listdir(dirPath)
for path in child_file_list:
    full_path = dirPath + "/" + path
    if os.path.isdir(full_path):
        print "======================{}========================".format(os.path.basename(path))
        find_unuse_image_in_tsx_file(full_path)
    else:
        pass