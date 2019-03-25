#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# 标准数据类型
# Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Dictionary（字典）

# 数字 
# del 删除一些对象的引用
var1 = 1
var2 = 10
del var1
# print var1    # 报错 'var1' is not defined
print var2

# 字符串
string = 'abcdefg '
print string[1:5]
print string[:]
print string * 2
print string + 'TEST'

# 列表
list = ['runoob', 789, 2.234, 'john', 70.2]
tinylist = [123, 'john']
print list
print list[0]
print list[1:3]
print tinylist * 2
print list + tinylist

# 元组 ==>> 元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ( 'runoob', 789, 23.3, 'john', 79.1)
tinytuple = (123, 'john')
print tuple
print tuple[0]
print tuple * 2
print tuple + tinytuple

# 字典
dict = {}
dict['one'] = 'this is one'
dict[2] = 'this is two'
tinydict = {'name': 'john', 
            'code': 234234,
            'dept': 'sales'}
print dict['one']
# print dict['three']  # error
print tinydict
print tinydict.keys()
print tinydict.values()
print tinydict.has_key('sss')

# 类型转换
temp_int = 10000
temp_string = '123'
temp_list = "[123, 3423, \"string\"]"

print int(temp_string, 10)
print str(temp_int)


