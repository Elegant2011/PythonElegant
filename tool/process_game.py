#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil as psutil
from pprint import pprint as pp

print('CPU信息')
print('cpu个数',psutil.cpu_count(logical=False))


print('进程信息')
proc = [p.info for p in psutil.process_iter(attrs=['pid', 'name'])]
for p in proc:
    if p['name'] == 'Registry':
        pp(p)