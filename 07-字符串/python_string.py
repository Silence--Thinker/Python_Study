#!/usr/bin/python
#-*- coding: utf-8 -*-

import math

print "\n * \r \000 \r \b \a \' \" \v \f"
print R"\n * \r \000 \r \b \a \' \" \v \f"


num = 100
num2 = 3.14
string = "this a string "

print "string: %s, num_01: %d, num_02: %f" %(string, num, num2)

print "float_num: %.4f" %(num2)


# 新型格式化方式 format
# http://www.runoob.com/python/att-string-format.html

print "新型格式化方式 format"
print "{} {}".format("hello", "world")
print "{0} {1}".format("hello", "world")
print "{0} {1}, {1}, {0}".format("hello", "world")

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

print "{:.2f}".format(math.pi)

hi = ''' hi
there'''
print hi

print "ABC".center(8)
print "ABC".zfill(8)
print "ABC".ljust(8)
print "ABC".rjust(8)

print "hello".find("ll", 0, -1)
print "hello 123412".isalnum()
print "hello123412".isalnum()
print "hello1".isalpha()
print "hello".isalpha()
print "123123".isdigit()
print "123123u".isdigit()

print "A".join(['123', 'abc'])

print "   ABC   DEF  ".lstrip()
print "   ABC   DEF  ".rstrip()
print "   ABC   DEF  ".strip()

print "ABC DEF FGH ADC".partition('A') # 第一个
print "ABC DEF FGH ADC BAC DFG".replace('A', 'Z', 2)

print "ABC DEF FGH ADC BAC DFG".split('A', 10)
print "ABC DEF FGH ADC BAC DFG".startswith('ABC')




