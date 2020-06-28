class Human2(object):  
    """
    拦截已存在的属性
    """  
    def __init__(self):
        self.age = 18
    def __getattribute__(self,item):
        # 通过print可知，getattribute截获的属性获取
        print('Human2:__getattribute__')

h1 = Human2()

h1.age
h1.noattr
