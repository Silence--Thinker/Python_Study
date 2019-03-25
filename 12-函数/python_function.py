#!/usr/bin/python
# -*- coding: utf-8 -*-

def printme (str):
    "打印"
    print str
    return

printme (str = "My STRING")


def printInfo (name, age = 35):
    "打印 name and age"
    print "Name: ", name
    print "Age: ", age
    return

printInfo(age = 28, name = "caoxiujin")
printInfo(name = "caoxiujin")
printInfo('cao')


# 不定长参数
# def functionname([formal_args,] *var_args_tuple ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]

def printallinfo (arg1, *vartuple):
    "打印所有传入的参数"
    print "输出：", arg1,
    for var in vartuple:
        print var, " ",
    print ""
    return

printallinfo (10, 123.123, "ABC")


# 匿名函数
# lambda函数的语法只包含一个语句，如下：
# lambda [arg1 [,arg2,.....argn]]:expression

sum = lambda arg1, arg2: arg1 + arg2
print "相加的值为：", sum(21, 10)

if __name__ == '__main__':
    print '主程序运行'
else:
    print 'package 初始化'

