#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

# ▶︎︎ re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
# 👉语法: re.match(pattern, string, flags=0)
# ● pattern: 匹配的正则表达式
# ● string: 要匹配的字符串。
# ● flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
print '============================== re.match =============================='
print re.match('www', 'www.km.sankuai.com').span()
print re.match('com', 'www.km.sankuai.com')

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print "matchObj.group(): ", matchObj.group()
    print "matchObj.group(1): ", matchObj.group(1)
    print "matchObj.group(2): ", matchObj.group(2)
    print "matchObj.groups: ", matchObj.groups()
else:
    print "No match !!"

# ▶︎︎ re.search 扫描整个字符串并返回第一个成功的匹配
# 👉语法: re.search(pattern, string, flags=0)
# ● pattern: 匹配的正则表达式
# ● string: 要匹配的字符串。
# ● flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
print '============================== re.search =============================='
print re.search('www', 'www.km.sankuai.com').span() # 在起始位置匹配
print re.search('com', 'www.km.sankuai.com').span() # 不在起始位置匹配

# ▶︎︎ re.match与re.search的区别
# 👉re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配
print '============================== re.match与re.search的区别 =============================='
line = 'Cats are smarter than dogs'
matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print "match --> matchObject.group(): ", matchObj.group()
else:
    print "match No match"
matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print "search --> matchObject.group(): ", matchObj.group()
else:
    print "search No match"

# 正则表达式对象
# ▶︎︎ re.RegexObject: 正则表达式对象
# ▶︎︎ re.compile() 返回 RegexObject 对象

# re.MatchObject: 正则匹配对象
# ▶︎︎ group() 返回被 RE 匹配的字符串
# ● start() 返回匹配开始的位置
# ● end() 返回匹配结束的位置
# ● span() 返回一个元组包含匹配 (开始,结束) 的位置


# ▶︎︎ re.RegexObject: 正则表达式对象



# 身份证匹配 分组标注组名 <?P>
s = '34112419920723606X'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})(?P<brith_day>\d{4})(?P<suffix>\w{4})',s)
print res.groupdict()
print res.groups()