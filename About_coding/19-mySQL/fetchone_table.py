#!/usr/bin/python
# -*- coding: utf-8 -*-

# mac 下操作MySQL:  https://www.jianshu.com/p/b13f99cbdf55
# python mysql 操作: https://www.runoob.com/python/python-mysql.html
# 操作相关表: employeeTable

# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall():接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。

import mysql.connector

# 打开数据库连接 （根据自己的用户名、密码及数据库名称进行修改）
mysqlDB = mysql.connector.connect(user="root", passwd="12345678", database="TESTDB", charset="utf8")

# 使用 cursor()方法获取操作游标
cursor = mysqlDB.cursor()

fetchone_sql = "SELECT * FROM employeeTable \
                WHERE INCOME > %s " % (1000)

try:
    cursor.execute(fetchone_sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    print cursor.rowcount
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print "fname=%s, lname=%s, age=%s, sex=%s, income=%s" % (fname, lname, age, sex, income)
except mysql.connector.errors.DataError as e:
    print '查询语句执行失败'
    print e
    mysqlDB.rollback()

mysqlDB.close()
