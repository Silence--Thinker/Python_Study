#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import socket

# 建立一个服务端
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print 'host: ' + host
port = 12345
# 绑定要监听的端口
socket_server.bind((host, port))

# 开始监听 可以使用5个链接排队
socket_server.listen(5)

# conn 就是客户端链接过来而在服务端为期生成的一个链接实例
times = 0
while True:
    # 等待链接，多个链接的时候会出现问题，其实返回了两个值
    conn, addr = socket_server.accept()
    print 'conn: %s, addr: %s' % (conn, addr)
    while times < 5:
        try:
            # 接收数据
            data = conn.recv(1024) 
            # 打印接收的数据
            print 'recive: ' +  data.decode()
            # 再发送数据
            conn.send(data.upper())
            times += 1
        except ConnectionResetError as e:
            print '关闭了正在占线的链接！'
            break
    if times >=5: break
    conn.close()