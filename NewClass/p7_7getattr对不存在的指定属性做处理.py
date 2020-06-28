class Human2(object):  
    def __init__(self):
        self.age = 18

    def __getattr__(self, item): 
        """
        fly属性返回'superman',其他属性返回None
        """
        print('Human2:__getattr__')
        self.item = item
        if self.item == 'fly':
            return 'superman'
        # return 'OK'

h1 = Human2()

print(h1.age)
print(h1.fly)
print(h1.noattr)


