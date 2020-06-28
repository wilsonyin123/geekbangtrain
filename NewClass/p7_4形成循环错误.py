class Human2(object):  
    """
    拦截已存在的属性
    """  
    def __init__(self):
        self.age = 18
    def __getattribute__(self,item):
        # print('Human2:__getattribute__')
        # 这里会返回RecursionError: maximum recursion depth
        #  exceeded while calling a Python object
        return self.__getattribute__(item)
h1 = Human2()

print(h1.age)



