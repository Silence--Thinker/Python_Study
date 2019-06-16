#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 👉 线程同步
# ▶︎ ︎使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，
#   对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间

# 👉 线程优先队列
# ▶︎ Python的Queue模块中提供了同步的、线程安全的队列类，
#   包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue
# ▶︎ Queue模块中的常用方法
# ● Queue.qsize() 返回队列的大小
# ● Queue.empty() 如果队列为空，返回True,反之False
# ● Queue.full() 如果队列满了，返回True,反之False
# ● Queue.full 与 maxsize 大小对应
# ● Queue.get([block[, timeout]])获取队列，timeout等待时间
# ● Queue.get_nowait() 相当Queue.get(False)
# ● Queue.put(item) 写入队列，timeout等待时间
# ● Queue.put_nowait(item) 相当Queue.put(item, False)
# ● Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
# ● Queue.join() 实际上意味着等到队列为空，再执行别的操作

import threading
import time

list = [0] * 12
class customThread (threading.Thread):
    def __init__ (self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
    def run (self):
        print "开始线程:", self.name
        # 获得锁
        threadLock.acquire()
        print_time(self.name, self.counter, list.__len__())
        # 释放锁
        threadLock.release()
    def __del__ (self):
        print self.name, "线程结束！"

def print_time (threadName, delay, counter):
    while counter:
        time.sleep(delay)
        list[counter - 1] += 1
        print "[%s] %s 修改第 %3d 个值, 修改后值为: %d" % (time.ctime(time.time()), threadName, counter, list[counter - 1])
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建线程
thread_1 = customThread(1, 'Thread-1', 1)
thread_2 = customThread(2, 'Thread-2', 1)

# 开启线程
thread_1.start()
thread_2.start()

# 添加线程到线程列表
threads.append(thread_1)
threads.append(thread_2)

# 等待所有线程完成
for t in threads:
    t.join()
print "主线程结束！"

