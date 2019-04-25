#!/usr/bin/python
# -*- coding: utf-8 -*-

# 浏览器URL：http://localhost/cgi-bin/hello.py

print "Content-type:text/html"
print ""           # 空行，告诉服务器结束头部
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title>我的第一个 CGI 程序！</title>'
print '</head>'
print '<body>'
print '<h2>Hello World! 我是来自菜鸟教程的第一CGI程序</h2>'
print '<h3>这是一个额外的小标题</h3>'
print '</body>'
print '</html>'