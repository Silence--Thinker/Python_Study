#!/usr/bin/python
# -*- coding: utf-8 -*-

# 浏览器URL：http://localhost/cgi-bin/checkbox.py?google=1

# CGI 处理模块
import cgi, cgitb

# 创建 FieldStorage的实例
form = cgi.FieldStorage()

# 获取数据
if form.getvalue('google'):
    google_flag = "是"
else:
    google_flag = "否"

if form.getvalue('baidu'):
    baidu_flag = "是"
else:
    baidu_flag = "否"

print "Content-type:text/html"
print ""           # 空行，告诉服务器结束头部

print '<html>'

print '<head>'
print '<meta charset="utf-8">'
print '<title> Python CGI checkbox 测试</title>'
print '</head>'

print '<body>'
print '<h2>Google 是否选择了 ： %s </h2>' % (google_flag)
print '<h2>Baidu 是否选择了 ： %s </h2>' % (baidu_flag)
print '</body>'

print '</html>'