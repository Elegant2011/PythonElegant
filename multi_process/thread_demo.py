#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   thread_demo.py
@Time    :   2020/02/11 18:10:49
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

import time
import threading as th


def loop():
    print('thread %s is running...' % th.current_thread().name)
    n = 0
    while n < 5:
        n = n +1
        print('thread %s >>> %s' % (th.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.' % th.current_thread().name)    

print('thread %s is running....' % th.current_thread().name)
t = th.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % th.current_thread().name)
