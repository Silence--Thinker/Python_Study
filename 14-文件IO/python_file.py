#!/usr/bin/python
#-*- coding: utf-8 -*-

file = open('temp.json', 'w')
print "文件名：", file.name
print "文件访问模式：", file.mode
print "文件是否关闭：", file.closed
print "末尾是否强制加空格 : ", file.softspace

file.write("{\n")
file.write(R' "name" : "caoxiujin",')
file.write("\n")
file.write(R' "age" : "28", ')
file.write("\n")
file.writelines([R' "sex"', " : ", R'"男"'])
file.write("\n}")

file.close()
print "文件是否关闭：", file.closed


file = open('temp.json', 'r+')
print "读取的字符串是：", file.read(10)
print "当前文件位置：", file.tell()

position = file.seek(2, 1)
print "当前文件位置：", file.tell()
print "重新读取字符串：", file.read(10)
file.close()


import os
os.rename("temp.json", "other.json")
print os.rmdir("test")
print os.mkdir("test")
print os.chdir("test")
print os.getcwd()
print os.chdir("../")
print os.getcwd()
