class Human2(object):  
    """
    拦截已存在的属性
    """  
    def __init__(self):
        self.age = 18
    def __getattribute__(self,item):
        # 通过print可知，getattribute截获的属性获取
        print('Human2:__getattribute__')
        return super().__getattribute__(item)
h1 = Human2()

print(h1.age)
# 存在的属性返回取值
print(h1.noattr)
# 不存在的属性返回 AttributeError:


