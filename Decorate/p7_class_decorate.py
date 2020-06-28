# Python 2.6 开始添加类装饰器
from functools import wraps

class MyClass(object):
    def __init__(self, var='init_var', *args, **kwargs):
        self._v = var
        super(MyClass, self).__init__(*args, **kwargs)
    
    def __call__(self, func):
        # 类的函数装饰器
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            func_name = func.__name__ + " was called"
            print(func_name)
            return func(*args, **kwargs)
        return wrapped_function

def myfunc():
    pass

MyClass(100)(myfunc)()
# 其他经常用在类装饰器的python自带装饰器
# classmethod
# staticmethod
# property


# 另一个示例
class Count:
    def __init__(self,func):
        self._func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kargs):
        self.num_calls += 1
        print(f'num of call is {self.num_calls}')
        return self._func(*args, **kargs)

@Count
def example():
    print('hello')

example()
print(type(example))


# 其他常用的排序和计数相关用法
a = (1, 2, 3, 4)
a.sort()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'sort'
sorted(a)
# [1, 2, 3, 4]
# sorted 支持更多场景  多维list 字典混合list list混合字典


# 计数有没有更优雅、更Pythonic的解决方法呢？
# 答案是使用collections.Counter。
from collections import  Counter
Counter(some_data)
# 利用most_common()方法可以找出前N个出现频率最高的元素以及它们对应的次数
Counter(some_data).most_common(2)


