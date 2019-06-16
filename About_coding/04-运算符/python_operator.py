#!/usr/bin/python
# -*- coding: utf-8 -*-

# python 运算符
# http://www.runoob.com/python/python-operators.html

# 算术运算符
# 比较（关系）运算符
# 赋值运算符
# 逻辑运算符 and or not
# 位运算符
# 成员运算符 in, not in
# 身份运算符 is, not is
# 运算符优先级

# * 八皇后问题 queen problem with recurison
BOARD_SIZE = 8

def under_attack(col, queens):
   left = right = col
   for r, c in reversed(queens):
 #左右有冲突的位置的列号
       left, right = left - 1, right + 1

       if c in (left, col, right):
           return True
   return False

def solve(n):
   if n == 0:
       return [[]]

   smaller_solutions = solve(n - 1)

   return [solution+[(n,i+1)]
       for i in xrange(BOARD_SIZE)
           for solution in smaller_solutions
               if not under_attack(i+1, solution)]

for answer in solve(BOARD_SIZE):
   print answer
        


