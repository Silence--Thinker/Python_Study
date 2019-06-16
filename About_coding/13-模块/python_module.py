#!/usr/bin/python
#-*- coding: utf-8 -*-


# Python 模块
# Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句

Money = 2000
def addMoney():
    "money + 1"
    global Money
    Money = Money + 1
    return

print Money, addMoney() or Money


import math
print dir(math)

