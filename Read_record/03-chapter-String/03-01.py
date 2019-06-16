#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 👉使用字符串格式设置运算符——百分号 ▶︎︎ 
format = "hello, %s. %s enough for ya"
values = ('world', 'hot')
string = format % values
print string
# hello, world. hot enough for ya

# 👉使用模板字符串，类似于UNIX shell的语法
# 等号的参数称为：关键字参数
from string import Template
temp1 = Template('Hello, $who, $what enough for ya')
temp1 = temp1.substitute(who='Mars', what='Dusty')
print temp1
# Hello, Mars, Dusty enough for ya

# 👉使用字符串方法format
# 1. 替换字段没有名称，或索引作为名称
string1 = "{}, {} and {}".format("first", "second", "third")
print string1 
# first, second and third
 
string2 = "{0}, {2} and {1}".format("first", "second", "third")
print string2
# first, third and second

# 2. 带有命名字段的格式化
from math import pi
string = "{name} is approximately {value:.2f}".format(value=pi, name="π")
print string
# π is approximately 3.14

# 3. 变量名和命名字段相同，可以简写 ==>>仅仅在Python 3.6或之后
from math import e
string = f"Euler's constant is roughly {e}."
print string