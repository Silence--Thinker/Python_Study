#!/usr/bin/python3
#-*- coding: utf-8 -*-

import requests
import os
import json

import Queue
import threading
import time

# 比较两个版本的大小
def compare_version (version_01, version_02):

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

def get_bundle_list ():
    clone = 'git archive --remote ssh://git@git.sankuai.com/reco/sc_mrn_bundle_name_list.git master -- bundle_name_list_c.json | tar -xO'
    outResult = os.popen(clone).read()
    return json.loads(outResult)

def request_get_versions(bundle_name, size, test=True):
    url = 'https://mrn.sankuai.com/api/{}/evaV2/listBundles?pageIndex=1&name={}&pageSize={}'.format('test' if test else 'production', bundle_name, size)
    response = requests.get(url=url).text
    response_json = json.loads(response)
    version_list = []
    if response_json and response_json['list']:
        info_list = response_json['list']
        for info in info_list:
            version_list.append(info['version'])
    pass
    return version_list

def cooking_version_info(bundle_dict, version_prefix='',queue=None):
    queueLock = threading.Lock()

    queueLock.acquire()
    if not queue.empty():
        bundle_name = queue.get()
        print('========================== {} =========================={}'.format(bundle_name, threading.currentThread().name))
        # get versions
        production_version_list = request_get_versions(bundle_name, 20, False)
        test_version_list = request_get_versions(bundle_name, 20, True)

        # filter version
        production_version_list = filter(lambda version: compare_version(version, version_prefix) != -1, production_version_list)
        test_version_list = filter(lambda version: compare_version(version, version_prefix) != -1, test_version_list)

        # sort version
        production_version_list.sort(cmp=compare_version,key=lambda n: n ,reverse=True)
        test_version_list.sort(cmp=compare_version,key=lambda n: n ,reverse=True)

        # get max version
        p_max_version = production_version_list[0] if len(production_version_list) else ''
        t_max_version = test_version_list[0] if len(test_version_list) else ''

        waring = False
        if p_max_version < t_max_version:
            waring = True
            pass
        bundle_dict[bundle_name] = {
            'name': bundle_name,
            't_versions': test_version_list, 
            'p_versions': production_version_list, 
            'waring': waring,
            'p_max_version': p_max_version,
            't_max_version': t_max_version
        }
        queueLock.release()
    else:
        queueLock.release()
    pass
pass

def main(version_prefix='7.32'):
    start_time = time.time()

    # 获取所有 bundle 名称
    bundle_list = get_bundle_list()
    # bundle_list = filter(lambda bundle: bundle.startswith('flashbuy-im-group'), bundle_list) 
    bundle_dict = {}

    print('============================ begaing ==============================')
    workQueue = Queue.Queue(len(bundle_list) * 2)
    queueLock = threading.Lock()
    threads = []

    # 1. 填充任务
    queueLock.acquire()
    for bundle in bundle_list:
        bundle_name = 'rn_supermarket_' + bundle
        workQueue.put(bundle_name)
        pass
    queueLock.release()    
    
    # 2. 创建线程 开启线程
    for bundle in bundle_list:
        thread = threading.Thread(target=cooking_version_info, args=(bundle_dict, version_prefix, workQueue), name=bundle)
        thread.start()
        threads.append(thread)
        pass
    # 3. 等待队列清空
    while not workQueue.empty():
        pass
    # 4. 等待所有线程完成
    for thread in threads:
        thread.join()
        pass
    print('============================ ending ==============================')
    # 得到最终的数据
    for bundle_name in bundle_dict.keys():
        info = bundle_dict[bundle_name]
        if info['waring'] == True:
            print('========================== {} =========================='.format(bundle_name))
            # print('======= 测试 =======')
            # for version in info['t_versions']:
            #     print('test', version)
            #     pass
            # print('======= 正式 =======')
            # for version in info['p_versions']:
            #     print('prod', version)
            #     pass
            print('{} 测试最大版本号为: {}, 正式最大版本号为:{}'.format(bundle_name, info['t_max_version'],info['p_max_version']))
            print('{}可能存在漏发正式环境的情况, 请确认是否漏发！！'.format(bundle_name))
            pass
        pass
    end_time = time.time()
    print('程序执行时间 time = {:.2f}秒'.format(end_time - start_time))
    return bundle_dict
    

if __name__ == "__main__":
    main()
