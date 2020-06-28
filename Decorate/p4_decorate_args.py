# 装饰器带参数 
from time import ctime,sleep

def outer_arg(bar):
    def outer(func):
        def inner(*args,**kwargs):
            print("%s called at %s"%(func.__name__,ctime()))
            ret = func(*args,**kwargs)
            print(bar)
            return ret
        return inner
    return outer

# 相当于outer_arg('foo_arg')(foo)()
@outer_arg('foo_arg')
def foo(a,b,c):
    return (a+b+c)
    
print(foo(1,3,5))

############################################

# 装饰器堆叠

@classmethod
@synchronized(lock)
def foo(cls):
    pass


def foo(cls):
    pass
foo = synchronized(lock)(foo)
foo = classmethod(foo)
