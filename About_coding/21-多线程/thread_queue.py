#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 案例: 创建三个线程，创建一个队列，每个线程不断的读取队列中是否有任务，如果有就去执行，
# 然后往队列里添加5个任务，看看分别是哪个线程执行了哪个任务？

import Queue
import threading
import time

exitFlag = 0

class customThread (threading.Thread):
    def __init__ (self, threadId, name, queue):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.queue = queue
    def run(self):
        print "Starting " + self.name
        process_data (self.name, self.queue)
        print "Ending " + self.name

    def __del__(self):
        print "线程结束 " + self.name

def process_data (threadName, queue):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = queue.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)

threadList = ['Thread-1', 'Thread-2', 'Thread-3']
workNameList = ['One', 'Two', 'Three', 'Four', 'Five']

queueLock = threading.Lock()
workQueue = Queue.Queue(10)

threads = []
threadId = 1

# 创建线程 开启线程
for threadName in threadList:
    thread = customThread(threadId, threadName, workQueue)
    thread.start()
    threads.append(thread)
    threadId += 1

# 填充线程
queueLock.acquire()
for work in workNameList:
    workQueue.put(work)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程退出
exitFlag = 1

# 等待所有线程完成
for thread in threads:
    thread.join()

print "Exiting Main Thread"