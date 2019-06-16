#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

# 身份证匹配 分组标注组名 <?P>
print '============================== 身份证匹配 =============================='
string = '34112419920723606X'
print '匹配字符串: ', string
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})(?P<brith_day>\d{4})(?P<suffix>\w{4})',string)
print res.groupdict()
print res.groups()


# OC import文件匹配
print '============================== OC import文件匹配 =============================='
string1 = 'import <UIKit/UIView.h>'
string2 = 'import "UIViewController.h"'
string3 = '@import Foundation'
string1 = '    import <UIKit/UIView.h>    '   
string2 = ' import "UIViewController.h"    '
string3 = '    @import Foundation        '
regexObj = re.compile(r'(?P<pre_fix>\s*@*import\s*)(?P<file_name><*"*\w*/*\w*.h*>*"*)(\s*)')
string_dict_01 = re.search(regexObj, string1).groupdict()
string_dict_02 = re.search(regexObj, string2).groupdict()
string_dict_03 = re.search(regexObj, string3).groupdict()

print string_dict_01
print string_dict_02
print string_dict_03

file_name_01 = string_dict_01['file_name']
file_name_02 = string_dict_02['file_name']
file_name_03 = string_dict_03['file_name']
print file_name_01, file_name_02, file_name_03

regexObj = re.compile(r'(\w*.h)')
print re.search(regexObj, file_name_01).groups()[0]
print re.search(regexObj, file_name_02).groups()[0]
# print re.search(regexObj, file_name_03).groups()

matchObj = re.finditer(r'(\s*import\s*)("\w*.h")', string2)
for match in matchObj: 
    print match.group() 