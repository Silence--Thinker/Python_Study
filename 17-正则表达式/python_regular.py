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

# ▶︎︎ re.sub: Python 的 re 模块提供了re.sub用于替换字符串中的匹配项
# 👉语法: re.sub(pattern, repl, string, count=0, flags=0)
# ● pattern: 正则中的模式字符串。
# ● repl: 替换的字符串，也可为一个函数。
# ● string: 要被查找替换的原始字符串。
# ● count: 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
print '============================== re.sub =============================='
phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
num = re.sub(r'#.*$', '', phone)
print "电话号码是：", num 
num = re.sub(r'\D', '', phone)
print "电话号码是：", num 

# ● repl: repl 参数是一个函数
def double (matchObj):
    value = int(matchObj.group('value'))
    print "value = ", value
    return str(value * 2)

string = 'A==23==G==4==HFD===567==='
print re.sub('(?P<value>\d+)', double, string)
print re.sub('(?P<value>\d)', double, string)


# ▶︎︎ re.compile: compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用
# 👉语法: re.compile(pattern[, flags])
# ● pattern: 一个字符串形式的正则表达式
# ● flags: 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
#   ● re.I 忽略大小写
#   ● re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
#   ● re.M 多行模式
#   ● re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
#   ● re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
#   ● re.X 为了增加可读性，忽略空格和 # 后面的注释
print '============================== re.compile =============================='
regexObj = re.compile(r'\d+')                       # 用于匹配至少一个数字  
print regexObj.match('one12twothree34four')         # match 默认从头开始匹配
print regexObj.match('one12twothree34four', 2)      # 从'e'的位置开始匹配，没有匹配
print regexObj.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配, 返回一个“match”对象
match = regexObj.match('one12twothree34four', 3, 10)
print match.group(0), match.start(0), match.end(0)  # 12, 3, 5


# ▶︎︎ re.findall: findall 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
# 👉语法: findall(string[, pos[, endpos]])
# ● string: 待匹配的字符串。
# ● pos: 可选参数，指定字符串的起始位置，默认为 0。
# ● endpos: 可选参数，指定字符串的结束位置，默认为字符串的长度。
print '============================== re.findall =============================='
regexObj = re.compile(r'\d+')
string = '2A=123= == 123BCDEFG== ==456'
print regexObj.findall(string)
print regexObj.findall(string, 3, 16)


# ▶︎︎ re.finditer: re.finditer和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
# 👉语法: re.finditer(pattern, string, flags=0)
# ● pattern: 匹配的正则表达式
# ● string: 要匹配的字符串
# ● flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
print '============================== re.finditer =============================='
matchObj = re.finditer(r"\d+", "12a32bc43jf3") 
for match in matchObj: 
    print match.group() 


# ▶︎︎ re.split: split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下
# 👉语法: re.split(pattern, string[, maxsplit=0, flags=0])
# ● pattern: 匹配的正则表达式
# ● string: 要匹配的字符串
# ● maxsplit: 分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数
# ● flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
print '============================== re.split =============================='
regexObj = re.compile(r'\W+')
string = '_123 A B.C/GHKH":K{OP}YU?>H'
print re.split(regexObj, string)
print re.split(regexObj, string, 2)
print re.split(r'a[\d+]', string)       # 对于一个找不到匹配的字符串而言，split 不会对其作出分割

# 正则表达式对象
# ▶︎︎ re.RegexObject: 正则表达式对象, 可以通过re.compile可生成，也可以是字符串
# ▶︎︎ re.compile() 返回 RegexObject 对象

# re.MatchObject: 正则匹配对象
# ▶︎︎ group() 返回被 RE 匹配的字符串
# ● start() 返回匹配开始的位置
# ● end() 返回匹配结束的位置
# ● span() 返回一个元组包含匹配 (开始,结束) 的位置

# ▶︎︎ re.RegexObject: 正则表达式对象

