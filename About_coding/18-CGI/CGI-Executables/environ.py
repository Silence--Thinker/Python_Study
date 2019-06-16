#!/usr/bin/python
# -*- coding: utf-8 -*-

# 浏览器URL：

import os

print "Content-type:text/html"
print ""           # 空行，告诉服务器结束头部

print '<html>'

print '<head>'
print '<meta charset="utf-8">'
print '<title> 环境变量 </title>'
print '</head>'

print '<body>'
print '<b> 环境变量 </b><br>'

print '<url>'
for key in os.environ.keys():
    print "<li><span style='color:green'>%30s </span> : %s </li>" % (key, os.environ[key])
print '<url>'

print '</body>'

print '</html>'