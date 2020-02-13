#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   communi_process.py
@Time    :   2020/02/11 17:39:13
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

from multiprocessing import Process,Queue
import os,time,random

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value )

if __name__=='__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr =Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()











