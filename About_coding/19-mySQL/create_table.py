#!/usr/bin/python
# -*- coding: utf-8 -*-

# mac 下操作MySQL:  https://www.jianshu.com/p/b13f99cbdf55
# python mysql 操作: https://www.runoob.com/python/python-mysql.html

import mysql.connector

# 打开数据库连接 （根据自己的用户名、密码及数据库名称进行修改）
mysqlDB = mysql.connector.connect(user="root", passwd="12345678", database="TESTDB", charset="utf8")

# 使用 cursor()方法获取操作游标
cursor = mysqlDB.cursor()

drop_sql = """
DROP TABLE IF EXISTS employeeTable
"""
cursor.execute(drop_sql)

creat_sql = """
CREATE TABLE employeeTable (
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT
)
"""
cursor.execute(creat_sql)

mysqlDB.close()