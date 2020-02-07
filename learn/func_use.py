from function_base import my_abs
from function_base import power
from function_base import enroll
from function_base import add_end
from function_base import calc
from function_base import calc_change
from function_base import person
from function_base import move
from function_base import lazy_sum
from function_base import now
from function_base import moveUse
#import sys
import datetime as dt
from function_base import fact

#print (sys.version_info)
print (dt.datetime.now())
print (my_abs(-78))

print ('8 * 8 = %d ' % power(8))

print ('---enroll : --- \n' )

print (enroll('Sarah','F'))

print (add_end())
print (add_end())
print (add_end())

# 不可变参数
print(calc([1,2,3]))

#可变参数
print(calc_change(1,3,5,7))

nums = [1,2,3]
print(nums)
print(calc_change(*nums))
print(calc(nums))

# 关键字参数
person('Michael',80)
person('Bob',101,city='shanghai')
person('Adam', 45, gender='M', job='Engineer')

extra ={'city':"Beijing",'job':"Engineer"}
person('Jack',35,**extra)

# 递归函数
print(fact(3))
print(fact(10))

# 汉诺塔问题
move(2,'A','B','C')
print('----------')
# moveUse(2,'A','B','C')
# move(3,'A','B','C')

# 返回函数作为参数
f = lazy_sum(1,3,5,7,9)
print(f)
print(f())


print (now())

