#!/usr/bin/python
# -*- coding: utf-8 -*-

# 浏览器URL：http://localhost/cgi-bin/save_file.py

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

fileItem = form['filename']

# 检测是否上传
file_path = ""
if fileItem.filename:
    # 设置文件路径
    fn = os.path.basename(fileItem.filename)
    open('/tmp/' + fn, 'wb').write(fileItem.file.read())
    message = "文件 '" + fn + "' 上传成功 "
    file_path = fileItem.filename
else:
    message = '文件没有上传'

print """\
Content-type:text/html

<html>
<head>
<meta charset="utf-8">
<title>Python save_file</title>
</head>

<body>
    <p>%s</p>
    <p>%s</p>
</body>

</html>
""" % (message, file_path)