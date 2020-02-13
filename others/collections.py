#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   collections.py
@Time    :   2020/02/12 22:15:11
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

from collections import namedtuple,deque,defaultdict
from collections import ChainMap,Counter
import os,argparse

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x,p.y)

q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

dd = defaultdict(lambda :'N/YY')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])

defaults = {
    'color': 'red',
    'user':'guest'
}

parser = argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args = {k : v for k,v in vars(namespace).items() if v}

combined = ChainMap(command_line_args,os.environ,defaults)

print('color=%s' % combined['color'])
print('user=%s' % combined['user'])


c = Counter('programming')
print(c)









