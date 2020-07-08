#!/usr/bin/python
#-*- coding: utf-8 -*-

# 比较两个版本的大小
def compare_version (version_01, version_02):

    if version_01 == version_02:
        return { 'result': '=', 'priority': 0 } 
    if version_01 and not version_02:
        return { 'result': '>', 'priority': 0 }
    if version_02 and not version_01:
        return { 'result': '<', 'priority': 0 }

    result = ''
    priority = 0
    v1_array = version_01.split('.')
    v2_array = version_02.split('.')

    version_count = min([v1_array.__len__(), v2_array.__len__()])
    i = 0
    while (i < version_count) :
        if (int(v1_array[i]) > int(v2_array[i])):
            result = '>'
            break
        elif (int(v1_array[i]) < int(v2_array[i])):
            result = '<'
            break
        else:
            result = '='
            i += 1
        pass
    pass
    if result == '=':
        priority = 0
    if not result == '=':
        priority = min(i, 2) + 1

    if result == '=':
        if (v1_array.__len__() > v2_array.__len__()):
            result = '>'
            priority = min(version_count + 1, 3)
        elif (v1_array.__len__() < v2_array.__len__()):
            result = '<'
            priority = min(version_count + 1, 3)
        pass
    pass
    return { 'result': result, 'priority': priority }


if __name__ == "__main__":
    version_01 = '1.2.3'
    version_02 = '1.2.0'
    result = compare_version(version_01, version_02)
    print("{} {} {} {}".format(version_01, result['result'], version_02, result['priority']))

    version_01 = '1.2.3'
    version_02 = '1.2.3.1'
    result = compare_version(version_01, version_02)
    print("{} {} {} {}".format(version_01, result['result'], version_02, result['priority']))

    version_01 = '2.3'
    version_02 = '1.2.0'
    result = compare_version(version_01, version_02)
    print("{} {} {} {}".format(version_01, result['result'], version_02, result['priority']))

    version_01 = '1.5.3'
    version_02 = '1.2.0.9'
    result = compare_version(version_01, version_02)
    print("{} {} {} {}".format(version_01, result['result'], version_02, result['priority']))

    version_01 = '1.2.3'
    version_02 = '1.2.0'
    result = compare_version(version_01, version_02)
    print("{} {} {} {}".format(version_01, result['result'], version_02, result['priority']))

    version_01 = ''
    version_02 = '1.0'
    result = compare_version(version_01, version_02)
    print("{} {} {} {}".format(version_01, result['result'], version_02, result['priority']))

    version_01 = '1.2'
    version_02 = '1'
    result = compare_version(version_01, version_02)
    print("{} {} {} {}".format(version_01, result['result'], version_02, result['priority']))
