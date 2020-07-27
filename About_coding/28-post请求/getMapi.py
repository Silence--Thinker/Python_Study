#!/usr/bin/python3
#-*- coding: utf-8 -*-

import requests
import json
import os
import re
import sys

import Queue
import threading
import time

class MapiDesc(object):
    
    def __init__(self, name='', description='', modelType='', ownersList=[]):
        self.name = name
        self.description = description
        self.modelType = modelType
        self.ownersList = ownersList

    # def __str__(self):
    #     return ' name = {},\n description = {},\n modelType = {},\n ownersList = {}'.format(self.name, self.name, self.modelType, self.ownersList)


def getMapiMap(mapi_name='', queue=None):
    queueLock = threading.Lock()
    queueLock.acquire()
    if queue.empty():
        queueLock.release()
        return
    mapiModelList = queue.get()

    url = 'https://mobile.sankuai.com/api/mapi/listApi'
    pyload = { 
        'appId': -1,
        'businessId': -1,
        'keyword': mapi_name,
        'pageNo': 1,
        'pageSize': 10,
        'version': ''
    }
    headers = {
        'Cookie': '_lxsdk=15e9d70043fc8-0c6bc8f54d242-143c6c55-13c680-15e9d70043fc8; _lxsdk_cuid=15f14a39141c8-0d4015d2344872-31657c00-13c680-15f14a39142c8; _ga=GA1.2.479591399.1509593777; gr_user_id=69202f1c-19bb-4d6b-9469-e73663bff822; uu=1171c7e0-f1ee-11e8-b422-95be39cc0e34; cid=1; ai=1; skmtutc=7OxCVcCKaLMxwOrVdZDKbd0CS3kl8JP9AzVv/kUdeLTWPcfcuhGI/SM5RmStvcKO-PFZY1iXH+VzVWVNiHDCXlTURBRg=; t_lxid=1716345a072c8-0fb4098cd83384-396a7f06-13c680-1716345a072c8-tid; UM_distinctid=1735bb0725a4e2-0c6730b9c5dbe7-31677402-1fa400-1735bb0725b5e5; af6315efa9_ssoid=eAGFjrtKA0EYRhlQCakkleWWyRbLzuWfi5XuboKll0Kwkdmdf0p9AQuTQrC100olYCHxCpKAQsAXELRRbNV9AAtLV8Ta7ivOdzg1Mv340iPBxeDhcxSxuvWSU0BvzWyQFxy9AxUrLAR3yhovQuPQaiud8Cp5Io3WKuYrBW7gFs8ok6KCZScFmmUJhUTPt1XaAQ26zYOr-_HoLmoS9q9Y_yTNTS4cX79-DaPFndvx803UI2F9amk53XTYaLz1T8rLo_fd04_DbnnWL8-7MxPB9nC_1fyF90jtL-yAREIZKY20uTN5YU2OgFoDxsYUXKIT6xQMME6ppCw2awFTnCtrgUIIIlbKelF9gVXbUS_tN47HZ_0**eAENx8ENACAIBLCVIHCC44gc-4-gST9dAYfwyJDq340Stzy22fe26LByVqL-QwFrcHb7WJB8THYSsg; JSESSIONID=699B56B52905620FC5171156A86F11A4',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    response = requests.post(url, data=json.dumps(pyload), headers=headers).text
    response_json = json.loads(response)
    dataList = response_json['data']['data']
    if not dataList:
        print('not dataList======= {} ======='.format(mapi_name))
    dataModel = dataList.pop(0)

    name = dataModel['name']
    description = dataModel['description']
    modelType = dataModel['modelType']
    ownersList = list(dataModel['ownersMap'].keys())
    if name.lower() == mapi_name.lower():
        model = MapiDesc(name, description, modelType, ownersList)
        mapiModelList.append(model)
    else:
        model = MapiDesc(name, description, modelType, ownersList)
        mapiModelList.append(model)
        print('======= {} {}======='.format(mapi_name, name))
    queueLock.release()

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

def getAllMapiModelList(rootPath):
    fileList = get_all_file(rootPath, '.ts$')
    mapiList = [os.path.split(file)[1].replace('_bin.ts', '.bin').replace('.ts', '.bin').replace('_', '/').lower() for file in fileList]
    liveImApi = ['msgsend.bin', 'joinchatroom.bin', 'leavechatroom.bin']
    roomApi = ['rtc/dial.bin', 'rtc/respond.bin', 'rtc/connect.bin', 'rtc/pushStreamSuccess.bin',
    'rtc/getPullStreamUrls.bin', 'startlive.bin', 'joinnewlive.bin', 'livegeneralinfo.bin',
    'stoplive.bin']
    # mapiList = liveImApi
    # mapiList = roomApi
    mapiList.sort()
    # mapiList = mapiList[0:4]
    # for name in mapiList:
    #     print(name)
    print(len(mapiList))
    # return []

    print('============================ begaing ==============================')
    workQueue = Queue.Queue(len(mapiList))
    queueLock = threading.Lock()
    threads = []

    mapiModelList = []
    # 1. 填充任务
    queueLock.acquire()
    for mapiName in mapiList:
        workQueue.put(mapiModelList)
        # 2.创建线程 开启线程
        thread = threading.Thread(target=getMapiMap, args=(mapiName, workQueue), name=mapiName)
        thread.start()
        threads.append(thread)
        pass
    queueLock.release()

    # 3. 等待队列清空
    while not workQueue.empty():
        pass
    # 4. 等待所有线程完成
    for thread in threads:
        thread.join()
        pass
    print('============================ ending ==============================')
    for model in mapiModelList:
        print('{}'.format(model.description))
    print(len(mapiModelList))
    return mapiModelList

def main():
    rootPath = '/Users/silence/Desktop/Working/flashbuy_mrn_mlive/src/platform/mapi/TSApis'
    mapiModelList = getAllMapiModelList(rootPath)
    # 写readme 文件
    with open('/Users/silence/Documents/GitHub/Python_Study/About_coding/28-post请求/README.md', 'w') as file:
        file.write('[toc]\n')
        file.write('## 接口文档\n')
        # 第一种打印方式
        # for model in mapiModelList:
        #     file.write('### {}\n'.format(model.name))
        #     file.write('**名称**\n\n')
        #     file.write('{}\n\n'.format(model.name))
        #     file.write('**描述**\n\n')
        #     file.write('{}\n\n'.format(model.description))
        #     file.write('**返回模型**\n\n')
        #     file.write('{}\n\n'.format(model.modelType))
        #     file.write('**接口负责人**\n\n')
        #     file.write('{}\n\n'.format(model.ownersList))

        #第二种打印方式
        file.write('||接口名称|接口描述|返回模型|接口负责人|\n')
        file.write('|:--|:--|:--|:--|:--|\n')
        index = 0
        for model in mapiModelList:
            index += 1
            ownersList = ''
            for author in model.ownersList:
                ownersList = '{}\t{}'.format(ownersList, author)
            file.write('|{}|{}|{}|{}|{}|\n'.format(index, model.name, model.description, model.modelType, ownersList))

    pass

if __name__ == "__main__":
    start_time = time.time()
    # 乱码的问题
    reload(sys)  
    sys.setdefaultencoding('utf8')
    main()

    end_time = time.time()
    print('程序执行时间 time = {:.3f}毫秒'.format((end_time - start_time) * 1000))
