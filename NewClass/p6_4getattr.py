class Human2(object):  
    """
    属性不在实例的__dict__中,__getattr__被调用
    """
    def __init__(self):
        self.age = 18

    def __getattr__(self, item): 
        print(f' __getattr__ called item:{item}')
        # 不存在的属性返回默认值 'OK'
        return 'OK'

h1 = Human2()

print(h1.age)
print(h1.noattr)