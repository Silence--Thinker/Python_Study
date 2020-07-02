#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import os
import re

# 获取目录下满足条件的文件
def get_file_path(dirPath, match):
	result_file_path = ''
	regexObj = re.compile(r'{}'.format(match))
	if os.path.exists(dirPath):
		pass
	else:
		return null
	if os.path.isdir(dirPath):
		child_file_list = os.listdir(dirPath)
        for file in child_file_list:
			file_path = dirPath + '/' + file
			if not os.path.isdir(file_path):
				if os.path.exists(file_path) and regexObj.search(file_path):
					result_file_path = file_path
	return result_file_path

# 是否是数字
def is_number(str):
    try:
        # 因为使用float有一个例外是'NaN'
        if str=='NaN':
            return False
        float(str)
        return True
    except ValueError:
        return False

def check_podspec():
	current_path = os.getcwd()
	podspec_file_path = get_file_path(current_path, '\.podspec$')

	if podspec_file_path:
		pass
	else:
		raise Exception('当前git 文件目录下没有找到.podspec文件，查看是否配置错误')
	
	error_note_lines = []
	missing_note_lines = []
	with open(podspec_file_path, 'r') as podspec_file:
		line = podspec_file.readline()
		line_index = 1
		
		while line:
			# rule = re.compile(r'(\s*s.dependency\s*)([^#].*,.*)(#\s*)(?P<ssss>(?:[^@ ].{1,}))(?P<ttt>(?:@[^ ]).{1,})((?: ){1,}\d$)')
			# match = re.search(rule, line)
			# if match:
				# print(line.strip(), '=====', line_index, '+++', match.groupdict()['ssss'], match.groupdict()['ttt'])
				# pass
			regexObj = re.compile(r'(?P<prefix>\s*s.dependency\s*)(?P<pod>[^#].*,.*)(?P<note>#.*)')
			matchObj = re.search(regexObj, line)
			if matchObj:
				note = matchObj.groupdict()['note']
				regexObj_note = re.compile(r'(^#)(?P<des>[^@]*)(?P<manager>(?:@[^ ]).{1,})(?P<priority>\s.{0,}\d$)')
				matchObj_note = re.search(regexObj_note, note.strip())
				if matchObj_note:
					# print('***', matchObj_note.groupdict()['des'], matchObj_note.groupdict()['manager'], matchObj_note.groupdict()['priority'])
					des = matchObj_note.groupdict()['des'].strip()
					manager = matchObj_note.groupdict()['manager']
					priority = matchObj_note.groupdict()['priority']
					if des and is_number(priority):
						pass
					else:
						error_note_lines.append({'line': line_index, 'content': line.strip(), 'reason': 'reason: 数字不正确' if des else 'reason: 依赖库描述缺失'})
					pass
				else:
					error_note_lines.append({'line': line_index, 'content': line.strip(), 'reason': 'reason: 缺失 @负责人员等'})
			else:
				regexObj_other = re.compile(r'(?P<prefix>^\s*s.dependency\s*)(.*)')
				if re.search(regexObj_other, line):
					missing_note_lines.append({'line': line_index, 'content': line.strip()})
				pass
			line = podspec_file.readline()
			line_index += 1
		pass
	# 获取文件名
	file_name = os.path.split(podspec_file_path)[1]
	out_msg = []
	if error_note_lines.__len__():
		for line_info in error_note_lines:
			out_info = "\033[1;31m File '{}', line {}, in '{} => 依赖注释不正确 {} \033[0m".format(file_name, line_info['line'], line_info['content'], line_info['reason'])
			out_msg.append(out_info)
	if missing_note_lines.__len__():
		for line_info in missing_note_lines:
			out_info = "\033[1;33m File '{}', line {}, in '{}' => 缺失依赖注释 \033[0m".format(file_name, line_info['line'], line_info['content'])
			out_msg.append(out_info)
	if out_msg.__len__():
		for out_info in out_msg:
			print(out_info)
		print("\033[1;32m 注释Demo:\n s.dependency 'SupermarketPlatform', '>=7.38.0.2'	 # 闪购平台库 @李道建 @冯阳 3 \033[0m")
		print("\033[1;32m # 依赖库描述 + @负责人员 + 数字(1:大版本 2:小版本两位 3:小版本三位) \033[0m")
		raise Exception('请正确的配置注释')
	return 0


if __name__ == "__main__":
    sys.exit(check_podspec())

