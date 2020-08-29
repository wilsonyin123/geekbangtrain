# GOD
class Human(object):  
    # 接收参数  
    def __init__(self, name):
        self.name = name

h1 = Human('Adam')
h2 = Human('Eve')


# 对实例属性做修改
h1.name = 'python'

# 对实例属性查询
h1.name

# 删除实例属性
del h1.name

# AttributeError，访问不存在的属性
# 由__getattribute__(self,name)抛出
h1.name



###################
class Human2(object):  
    """
    getattribute对任意读取的属性进行截获
    """  
    def __init__(self):
        self.age = 18
    def __getattribute__(self,item):
        print(f' __getattribute__ called item:{item}')

h1 = Human2()

h1.age
h1.noattr



