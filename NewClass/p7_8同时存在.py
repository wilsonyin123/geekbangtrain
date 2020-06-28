class Human2(object):    
    """
    所有的属性都能得到返回
    """
    def __init__(self):
        self.age = 18

    def __getattr__(self, item): 

        print('Human2:__getattr__')
        return 'Err 404 ,你请求的参数不存在'

    def __getattribute__(self, item):
        print('Human2:__getattribute__')
        return super().__getattribute__(item)

h1 = Human2()

# __getattribute__ 返回存在的属性，如果不存在抛出  AttributeError 异常，继续访问__getattr__函数
# 如果同时存在，执行顺序是 __getattribute__ > __getattr__ > __dict__
print(h1.age)
print(h1.noattr)
# 注意输出，noattr的调用顺序


