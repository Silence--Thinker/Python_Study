#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import os
import re
import json
import csv

# 比较两个版本的大小
def compare_version_release (version_01, version_02):

    if version_01 == version_02:
        return 0
    if version_01 and not version_02:
        return 1
    if version_02 and not version_01:
        return -1

    result = 0
    v1_array = version_01.split('.')
    v2_array = version_02.split('.')
    v1_count = len(v1_array)
    v2_count = len(v2_array)

    version_count = min([v1_count, v2_count])
    i = 0
    while (i < version_count) :
        if (int(v1_array[i]) > int(v2_array[i])):
            result = 1
            break
        elif (int(v1_array[i]) < int(v2_array[i])):
            result = -1
            break
        else:
            result = 0
            i += 1
        pass
    pass

    if result == 0:
        if (v1_count > v2_count):
            result = 1
        elif (v1_count < v2_count):
            result = -1
        pass
    pass
    return result
pass

def filechange ():
    json_file = './version_01.json'
    file_data = ''
    with open(json_file, 'r') as file:
        line = file.readline()
        while line:
            list = line.split(',')
            if len(list) > 1:
                line = '  "{}": "{}",\n'.format(list[0].strip(), list[1].strip())
            file_data += line
            line = file.readline()
    with open(json_file, 'w') as f:
        f.write('{\n')
        
        f.write(file_data)
        f.write('}\n')
    
def get_file_dict(): 
    json_file_01 = './version_01_live.json'
    json_file_02 = './version_02_wm.json'
    json_file_03 = './version_03_dp.json'
    dict_01 = {}
    dict_02 = {}
    dict_03 = {}
    with open(json_file_01, 'r') as load_f:
        dict_01 = json.load(load_f)

    with open(json_file_02, 'r') as load_f:
        dict_02 = json.load(load_f)
    
    with open(json_file_03, 'r') as load_f:
        dict_03 = json.load(load_f)
    return dict_01, dict_02, dict_03

def main ():
    version_list = []
    dict_01, dict_02, dict_03 = get_file_dict()
    for name_01, version_01 in dict_01.items():
        newDict = { 'name': name_01, 'version_live': version_01, 'version_wm': '', 'version_dp': '' } # 'version_live': version_01
        version_list.append(newDict)
        for name_02, version_02 in dict_02.items():
            if name_01 == name_02:
                newDict['version_wm'] = version_02
                pass
            pass
        pass
        for name_03, version_03, in dict_03.items():
            if name_01 == name_03:
                newDict['version_dp'] = version_03
                pass
            pass
    pass
    result_file_path =  './result.csv'
    with open(result_file_path, 'w') as csvfile:
        tableNames = [
            'name',
            'version_live', # InstaLive 依赖版本
            'version_wm',# waimai当前版本
            'version_dp'
        ]
        writer = csv.DictWriter(csvfile, tableNames)
        #注意header是个好东西
        writer.writeheader()
        for csvRow in version_list:
            # print('===', csvRow)
            if csvRow['version_wm'] == csvRow['version_dp'] or csvRow['version_wm'] == csvRow['version_live']:
                pass
            else:

                # if compare_version_release(csvRow['version_wm'], csvRow['version_live']) > 1 or compare_version_release(csvRow['version_wm'], csvRow['version_dp']) > 1:
                #     pass
                # else:
                writer.writerow(csvRow)
    pass
pass
            
if __name__ == "__main__":
    main()
