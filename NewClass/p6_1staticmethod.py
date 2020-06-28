import datetime
class Story(object):
    snake = 'Python'
    def __init__(self, name):
        self.name = name
    # 静态的方法
    @staticmethod
    def god_come_go():
        if datetime.datetime.now().month % 2 :
             print('god is coming')
    
Story.god_come_go()

# 静态方法可以由类直接调用
# 因为不传入self 也不传入 cls ，所以不能使用类属性和实例属性

