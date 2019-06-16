#!/usr/bin/python
#-*- coding: utf-8 -*-

import time

print "当前时间戳：", time.time()
print "本地时间为：", time.localtime(time.time())

print "本地时间为：", time.asctime(time.localtime())

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

import calendar
# 日历
print "输出2016年1月月的日历：", calendar.month(2019, 3)

print calendar.calendar(2019, 4, 1, 10)
print calendar.firstweekday()
print calendar.isleap(2019)
print calendar.monthcalendar(2019, 3)
print calendar.monthrange(2019, 3)
print calendar.monthrange(2019, 2)
print calendar.monthrange(2019, 4)

