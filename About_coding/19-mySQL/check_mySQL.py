#!/usr/bin/python
# -*- coding: utf-8 -*-

# mac 下操作MySQL:  https://www.jianshu.com/p/b13f99cbdf55
# python mysql 操作: https://www.runoob.com/python/python-mysql.html

# if you want check MySQLdb is working
# you can in terminal input: 
# python 
# import MySQLdb
# if not error, you succeed

import mysql.connector

# 打开数据库连接 （根据自己的用户名、密码及数据库名称进行修改）
mysqlDB = mysql.connector.connect(user="root", passwd="12345678", database="TESTDB", charset="utf8")

# 使用 cursor()方法获取操作游标
cursor = mysqlDB.cursor()

# 使用 execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
print 'Database version : %s ' % data

# 执行sql语句
mysqlDB.close()


