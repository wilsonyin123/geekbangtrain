# 被修饰函数带参数
from time import ctime,sleep

def outer(func):
    def inner(a,b):
        print("%s called at %s"%(func.__name__,ctime()))
        print(a,b)
        func(a,b)
    return inner

@outer
def foo(a,b):
    print(a+b)
    print("%s called at %s"%(foo.__name__,ctime()))
    
    
foo(1,2)
sleep(2)
foo(3,4)
foo.__name__

############################################

# 被修饰函数带不定长参数
from time import ctime,sleep

def outer2(func):
    def inner2(*args,**kwargs):
        print("%s called at %s"%(func.__name__,ctime()))
        func(*args,**kwargs)
    return inner2

@outer2
def foo2(a,b,c):
    print(a+b+c)
    
foo2(1,3,5)
sleep(2)
foo2(1,2,3)

############################################

# 被修饰函数带返回值
from time import ctime,sleep

def outer3(func):
    def inner3(*args,**kwargs):
        print("%s called at %s"%(func.__name__,ctime()))
        ret = func(*args,**kwargs)
        return ret
    return inner3

@outer3
def foo3(a,b,c):
    return (a+b+c)
    
print(foo3(1,3,5))