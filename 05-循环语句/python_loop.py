#!/usr/bin/python
#-*- coding: utf-8 -*-

import math

for num in range(1, 10):
    print num, " ",
print ""

# 求素数
max_num = 100
i = 2
while (i < max_num):
    j = 2
    is_su = True
    while (j <= math.sqrt(i)):
        if not (i % j): 
            is_su = False 
            break
        j += 1
    if is_su: print i , "是素数"
    i += 1

print dir(math)