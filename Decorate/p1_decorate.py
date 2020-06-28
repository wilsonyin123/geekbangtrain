# PEP 318 装饰器  PEP-3129 类装饰器

# 前置问题
def func1():
    pass
a=func1
b=func1()

# func1 表示函数
# func1() 表示执行函数

############################
# 装饰器, @ 语法糖
@decorate   
def func2():
    print('do sth')

# 等效于下面
def func2():
    print('do sth')
func2 = decorate(func2)

#############################







# 装饰器在模块导入的时候自动运行
# testmodule.py
def decorate(func):
    print('running in modlue')
    def inner():
        return func()
    return inner

@decorate
def func2():
    pass

# test.py
import testmodule
# from testmodule import func2

