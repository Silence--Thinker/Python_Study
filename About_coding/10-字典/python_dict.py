#!/usr/bin/python
#-*- coding: utf-8 -*-

dict = {'name': 'caoxiujin', 'age': 20, 'career': 'engineer'}
print dict
print dict['name']
print dict['career']
print len(dict)
print str(dict)
print type(dict)
print type(12.0)

print dict.copy()
print dict.fromkeys(['key_1', 'key_2'], 'value')
print dict.get('sex', '男')
print dict.has_key('sex')
print dict.keys(), dict.values()

print dict.pop('age', '28')
print dict