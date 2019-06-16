#!/usr/bin/python
# -*- coding: utf-8 -*-

# python 是强对齐语言，代码块不需要使用{}括号

print("hello world")
print("你好，世界")

if True:
    print "true"
else:
    print "false"

if True:
    print "true"
else:
    print "false"
    print "double false"

print "error"

one = 3
two = 4
three = 5
total = one + \
        two + \
        three
print total

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print days

paragraph = """这是一个可以
折行的字符串
"""
print paragraph
'''
这个是
一个多
行注释
'''

"""
这个也是一个多行
注释
"""

raw_input("按下enter键退出， 其他键显示...\n")
