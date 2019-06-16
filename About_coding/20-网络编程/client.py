#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import socket

# 申明socket类型，同时生成链接对象
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345
# 建立一个链接，链接到本地
socket_client.connect((host, port))
times = 0
while times < 5:
    # addr = socket_client.accept()
    # print '链接地址：', addr
    msg = "欢迎访问我的服务器！"
    # 发送一条消息 Python3 只接收btye流
    socket_client.send(msg.encode('utf-8'))
    # 接收一个信息，并指定接收的大小 为1024字节
    data = socket_client.recv(1024)
    # 输出接收信息
    print 'recv: ' + data.decode()
    times += 1
socket_client.close()