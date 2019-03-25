#!/usr/bin/python
#-*- coding: utf-8 -*-


list = []
list.append('Google')
list.append("Runoob")
print list

list1 = ['A', 'B', 'C']
list2 = ['A', 'B', 'C', 'D']
print cmp(list1, list2), " ", len(list1), " ", max(list1), " "

print list1.count('A')
print list1.index('C')

list1.sort()
print list1
list1.sort(reverse=True)
print list1
