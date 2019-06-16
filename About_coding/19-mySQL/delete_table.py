#!/usr/bin/python
# -*- coding: utf-8 -*-

# mac 下操作MySQL:  https://www.jianshu.com/p/b13f99cbdf55
# python mysql 操作: https://www.runoob.com/python/python-mysql.html
# 操作相关表: employeeTable

import mysql.connector

# 打开数据库连接 （根据自己的用户名、密码及数据库名称进行修改）
mysqlDB = mysql.connector.connect(user="root", passwd="12345678", database="TESTDB", charset="utf8")

# 使用 cursor()方法获取操作游标
cursor = mysqlDB.cursor()

delete_sql = "DELETE FROM employeeTable \
              WHERE INCOME <= %s " % (1000)
try:
    cursor.execute(delete_sql)
    mysqlDB.commit()
except mysql.connector.errors.DataError as e:
    print "删除数据失败"
    print e
    mysqlDB.rollback()
    
mysqlDB.close()