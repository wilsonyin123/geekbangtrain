class Human2(object):  
    def __init__(self):
        self.age = 18

    def __getattr__(self, item): 
        """
        不存在的属性返回'OK'
        """
        print('Human2:__getattr__')
        return 'OK'

h1 = Human2()

print(h1.age)
print(h1.noattr)


