#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   multi.py
@Time    :   2020/02/10 19:50:24
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

import os 
from multiprocessing import Pool
import time,random




def long_time_task(name):
    print('Run task %s (%s)' % (name,os.getpid()))
    start= time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end -start)))


if __name__ == "__main__":
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range (5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done.')





def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


# if __name__=='__main__':
#     # print(os.name)
#     print('Parent process %s.'% os.getpid())
#     p = Process(target=run_proc,args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('child process end.')











# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid ==0:
#     print('I am child process(%s) and my parent is %s.' %
#     (os.getpid(),os.getpid())
#     )
# else:
#     print('I (%s) just create a child process (%s).' % (os.getpid(),pid))


