#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Python通过两个标准库thread和threading提供对线程的支持。
# thread提供了低级别的、原始的线程以及一个简单的锁.
# 👉 threading 模块提供的其他方法：
# ● threading.currentThread(): 返回当前的线程变量。
# ● threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# ● threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

# 👉除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
# ▶︎︎ run(): 用以表示线程活动的方法。
# ▶︎︎ start():启动线程活动。
# ▶︎︎ join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# ▶︎︎ isAlive(): 返回线程是否活动的。
# ▶︎︎ getName(): 返回线程名。
# ▶︎︎ setName(): 设置线程名。

import threading
import time

exitFlag = 0

# customThread 继承父类：threading.Thread
class customThread (threading.Thread): 
    def __init__ (self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run (self):
        print "Starting", self.name
        print_time(self.name, self.counter, 5)
        print "Ending", self.name
    def __del__(self):
        print self.name, self.threadID, " 线程结束"

def print_time (threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

#创建线程
thread_01 = customThread(1, 'Thread_1', 1)
thread_02 = customThread(2, 'Thread_2', 2)

# 开启线程
thread_01.start()
thread_02.start()

print "Exiting Main Thread"
