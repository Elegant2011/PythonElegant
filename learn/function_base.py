def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def no_use():
    print(my_abs(90))
    print(my_abs(-90))


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def enroll(name, gender, age=6, city='BeiJing'):
    print('name', name)
    print('gender', gender)
    print('age', age)
    print('city', city)
    return " enroll end"


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


def calc(number):
    sum = 0
    for x in number:
        sum = sum + x * x
    return sum


def calc_change(*number):
    sum = 0
    for x in number:
        sum = sum + x * x
    return sum


def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)

def product(*args):
    x = 1
    if len(args)==0:
       raise TypeError()
    for i in args:
      x = i * x
    return x

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

# 汉诺塔问题
def move(n,a,b,c):
    if n == 1:
     print (n,a,'-->',c)
    else:
      move(n-1,a,c,b)
      print (n,a,'-->',c)
      move(n-1,b,a,c)