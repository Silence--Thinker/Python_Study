#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Python 中列表的详细解读
示例 2-1 代码
"""
months = [
		'January',
		'February',
		'March',
		'April',
		'May',
		'June',
		'July',
		'August',
		'September',
		'October',
		'November',
		'December'
	]
	# 一个列表，其中包含1-31对应的结尾
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 7 * ['th'] \
        + ['st']
year = input('Year: ')
month = input('Month (1-12): ')
day = input('day (1-31): ')

month_number = int(month)
day_number = int(day)

# 将月和日的数减1，才能得到正确的索引
month_name = months[month_number - 1]
ordinal = "%s" % day +  endings[day_number - 1]

print(month_name + ' ' + ordinal + ', ' + "%s" % year)
