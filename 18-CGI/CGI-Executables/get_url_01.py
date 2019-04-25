#!/usr/bin/python
# -*- coding: utf-8 -*-

# 浏览器URL：http://localhost/cgi-bin/get_url_01.py?name=Python_CGI_GET_请求&url=www.baidu.com

# CGI 处理模块
import cgi, cgitb

# 创建 FieldStorage的实例
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print "Content-type:text/html"
print ""           # 空行，告诉服务器结束头部

print '<html>'

print '<head>'
print '<meta charset="utf-8">'
print '<title> Python CGI GET 请求 测试</title>'
print '</head>'

print '<body>'
print '<h2> 测试名称：%s url地址：%s </h2>' % (site_name, site_url)
print '</body>'

print '</html>'