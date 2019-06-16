#!/usr/bin/env python
# -*- coding:utf-8 -*-

print "{foo} {1} {bar} {0}".format(1, 2, bar=4, foo = 3)
# 3 2 4 1

# print("{pi!s} {pi!r} {pi!a}".format(pi="π"))

string = "The number is {num}".format(num=42)
print string
# The number is 42

# 浮点数
string = "The number is {num:f}".format(num=42)
print string
# The number is 42.000000

# 二进制数
string = "The number is {num:b}".format(num=42)
print string
# The number is 101010
