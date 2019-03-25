#!/usr/bin/python
#-*- coding: utf-8 -*-


list_temp = []
list_temp.append('Google')
list_temp.append("Runoob")
print list_temp

list1 = ['A', 'B', 'C']
list2 = ['A', 'B', 'C', 'D']
print cmp(list1, list2), " ", len(list1), " ", max(list1), " "

print list1.count('A')
print list1.index('C')

list1.sort()
print list1
list1.sort(reverse=True)
print list1

array = list('ABCDEFG')
array.append('H')
print array
array.pop()
print array

array2 = list('HIJK')
array2.reverse()
array.extend(array2)
print array, ", length: ",len(array)

#  排序
array_tmep = sorted(array)
print "sorted排序：", array_tmep, "\n", array

array.sort()
print "sort排序", array

del array, array2, array_tmep

array = list(['11231', '123123', '12', '1', 'BKHK', 'jjljlj;', 'kjaljdfa'])
array_tmep = sorted(array, key = len, reverse = True)
print "sorted排序：", array_tmep, "\n", array

array.sort(key = len, reverse=False)
print "sort排序", array



