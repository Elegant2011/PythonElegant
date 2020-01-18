def my_abs(x):
    if x >=0:
        return x
    else:
        return -x

def no_use():
    print(my_abs(90))
    print(my_abs(-90))


def power(x,n=2):
    s =1 
    while n >0:
        n = n -1
        s = s * x
    return s

