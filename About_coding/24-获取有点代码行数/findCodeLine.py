#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import re
import csv
import json
from config import Team, CodeLanguage, Source, Table, FILETYPE_DICT, sourceList
# import sys
# reload(sys)   
# sys.setdefaultencoding('utf8')

# 代码拉取存储地
sourcePath = "/Users/silence/Desktop/Temp/source"

# 获取目录下满足条件的文件
def get_all_file(dirPath, match):
    file_path_list = []
    regexObj = re.compile(r'{}'.format(match))
    if os.path.exists(dirPath):
        pass
    else:
        return file_path_list
    if os.path.isdir(dirPath):
        child_file_list = os.listdir(dirPath)
        for file in child_file_list:
            file_path = dirPath + '/' + file
            if os.path.isdir(file_path):
                file_path_list = file_path_list + get_all_file(file_path, match)
            elif os.path.exists(file_path) and regexObj.search(file_path):
                file_path_list.append(file_path)
            else:
                pass
    return file_path_list

# 克隆代码
def git_clone(dict, sourcePath):
    os.chdir(sourcePath)
    name = dict[Source.name]
    code_dir = sourcePath + '/' + name
    clone = ''
    if os.path.exists(code_dir):
        # 文件夹存在直接切分支
        os.chdir(code_dir)
        clone = "git add . && git stash && git checkout {}".format(dict[Source.branch])
    else:
        # 文件夹不存在克隆代码
        clone = "git clone {} -b {} {}".format(dict.get(Source.git), dict[Source.branch], dict[Source.name])
    os.system('pwd')
    sheelStr = os.popen(clone).read()
    print(sheelStr)

# 检查注释代码项等数据
def find_all_valid_code(source_dict, sourcePath):
    # 1. 克隆代码
    git_clone(source_dict, sourcePath)
    code_dir = sourcePath + '/' + source_dict[Source.name]
    os.chdir(code_dir)

    # 2. 获取到满足条件的文件
    file_list = get_all_file(code_dir + source_dict[Source.chdir], FILETYPE_DICT[source_dict[Source.type]])
    print("{}仓库中共有: {}个{}文件".format(source_dict[Source.name], file_list.__len__(), FILETYPE_DICT[source_dict[Source.type]]))

    # 3. 排查注释代码和有效代码行数
    all_lineCount = 0
    all_validCount = 0
    all_commentCount = 0
    all_spaceCount = 0

    for file_path in file_list:
        comment_line = 0
        # 1. 读注释文本读出来 多少行
        with open(file_path, "r") as codeFile:
            all_line_str = codeFile.read()
            regexObj = re.compile(r'(?:[^\n]*//[^\n]*|/\*(?:(?!\*/).)*\*/)', re.DOTALL)
            match_comment = regexObj.findall(all_line_str)
            for target in match_comment:
                line = target.split('\n').__len__()
                comment_string = target.strip()
                is_comment_start = comment_string.startswith('//') or comment_string.startswith('/*')
                if (line == 1 and not is_comment_start):
                    # print("{}, 不计入注释行 {}=={}".format(comment_string, line, is_comment_start))
                    pass
                else:
                    comment_line = comment_line + line
                # print ("注释文本内容:{}, {}".format(target, line))
                pass
            # print("注释行数{}===".format(comment_line))
        pass

        lineCount = 0
        spaceCount = 0
        with open(file_path, 'r') as codeFile:
            line = codeFile.readline()
            while line:
                if line.strip() == '':
                    spaceCount = spaceCount + 1
                lineCount = lineCount + 1
                line = codeFile.readline()
            # print("代码行数: {}===空行数: {}".format(lineCount, spaceCount))
        all_lineCount = all_lineCount + lineCount
        all_commentCount = all_commentCount + comment_line
        all_spaceCount = all_spaceCount + spaceCount
        pass
    all_validCount = all_lineCount - all_commentCount - all_spaceCount
    # print("代码总行数: {}===".format(all_lineCount))
    # print("有效代码行数: {}===".format(all_validCount))
    # print("注释总行数: {}===".format(all_commentCount))
    # print("空行总数: {}===".format(all_spaceCount))

    # 4. 写入csv里
    valid = float(all_validCount) / float(all_lineCount)
    source_dict['all_lineCount'] = all_lineCount
    source_dict['all_validCount'] = all_validCount
    source_dict['all_commentCount'] = all_commentCount
    source_dict['all_spaceCount'] = all_spaceCount
    source_dict['valid'] = '{:.2f}%'.format(valid * 100.0)

# 处理数据
def cookingDataGetValidRate(dataList):
    comment_rate = 0
    code_rate = 0
    line_count = 0
    comment_count = 0
    code_count = 0
    for csvRow in dataList:
        line_count = line_count + csvRow[Table.lineCount.value]
        comment_count = comment_count + csvRow[Table.commentCount.value]
        code_count = code_count + csvRow[Table.codeCount.value]
        pass
    comment_rate = float(comment_count) / float(line_count) if line_count else 0
    code_rate = float(code_count) / float(line_count) if line_count else 0
    for csvRow in dataList:
        csvRow[Table.commentRatePlatform.value] = "{:.2f}%".format(comment_rate * 100)
        csvRow[Table.codeRatePlatform.value] = "{:.2f}%".format(code_rate * 100)
    pass

def main(sourceList, sourcePath):
    current_path = os.getcwd()
    if not sourcePath:
        sourcePath = current_path
    # 获取数据
    for source_dict in sourceList:
        find_all_valid_code(source_dict, sourcePath)
        pass
    # 整理数据
    iOS_B = []
    android_B = []
    JS_B = []

    iOS_C = []
    android_C = []
    JS_C = []
    for source_dict in sourceList:
        current_list = []
        # 团队
        if source_dict[Source.team] == Team.C:
            # 平台
            if source_dict[Source.type] == CodeLanguage.iOS:
                current_list = iOS_C
            elif source_dict[Source.type] == CodeLanguage.Android:
                current_list = android_C
            else:
                current_list = JS_C
            pass
        else:
            if source_dict[Source.type] == CodeLanguage.iOS:
                current_list = iOS_B
            elif source_dict[Source.type] == CodeLanguage.Android:
                current_list = android_B
            else:
                current_list = JS_B
        pass
        rowInfo = {Table.team.value: "{}端".format(source_dict[Source.team].name),
            Table.platform.value: source_dict[Source.type].name,
            Table.gitName.value: source_dict[Source.name],
            Table.branch.value: source_dict[Source.branch],
            Table.lineCount.value: source_dict['all_lineCount'],
            Table.codeCount.value: source_dict['all_validCount'],
            Table.commentCount.value: source_dict['all_commentCount'],
            Table.spaceCount.value: source_dict['all_spaceCount'],
            Table.codeRate.value: source_dict['valid']
        }
        current_list.append(rowInfo)
        pass
    # 处理平台数据
    cookingDataGetValidRate(iOS_B)
    cookingDataGetValidRate(android_B)
    cookingDataGetValidRate(JS_B)

    cookingDataGetValidRate(iOS_C)
    cookingDataGetValidRate(android_C)
    cookingDataGetValidRate(JS_C)

    ## 重新组合数据
    all_data_list = []
    all_data_list.extend(iOS_C)
    all_data_list.extend(android_C)
    all_data_list.extend(JS_C)
    all_data_list.extend(iOS_B)
    all_data_list.extend(android_B)
    all_data_list.extend(JS_B)

    result_file_path = current_path + '/' + 'result.csv'
    with open(result_file_path, 'w') as csvfile:
        tableNames = [
            Table.team.value, 
            Table.platform.value, 
            Table.codeRatePlatform.value, 
            Table.commentRatePlatform.value,
            Table.gitName.value, 
            Table.branch.value, 
            Table.lineCount.value, 
            Table.codeCount.value, 
            Table.commentCount.value, 
            Table.spaceCount.value, 
            Table.codeRate.value
        ]
        writer = csv.DictWriter(csvfile, tableNames)
        #注意header是个好东西
        writer.writeheader()
        for csvRow in all_data_list:
            writer.writerow(csvRow)
    pass

if __name__ == "__main__":
    main(sourceList, sourcePath)
    # for name, member in Table.__members__.items():
    #     print("name={}=={}=={}".format(name, member, member.value))

# platform = '平台'
# codeRatePlatform = '有效代码率(代码行/总行数)'
# commentRatePlatform ='注释率(注释行/总行数)'
# gitName = '库名称'
# branch = '分支'
# lineCount = '代码总行数'
# codeCount = '有效代码行数'
# commentCount = '注释总行数'
# spaceCount = '空行总数'
# codeRate = '有效代码比'

# print("\033[1;31m 字体颜色：红色\033[0m")
# print("\033[1;32m 字体颜色：深黄色\033[0m")
# print("\033[1;33m 字体颜色：浅黄色\033[0m")