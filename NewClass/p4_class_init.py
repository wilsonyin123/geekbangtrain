# GOD
class Human(object):
    
    # 使用__init__接收参数，思考不定参数处理
    def __init__(self, name):
        # self表示对象本身，约定俗成
        self.name = name

h1 = Human('Adam')
h2 = Human('Eve')


# 对实例属性做修改
h1.name = 'python'
h1.name
h2.name

