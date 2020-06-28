# 让实例的方法成为类的方法
class A(object):
    bar = 1
    def foo(self):
        print('in foo')
    # 使用类属性、方法
    @classmethod
    def class_foo(cls):
        print(cls.bar)
        cls().foo()

A.class_foo()
a = A()

#########################
class Story(object):
    snake = 'Python'
    def __init__(self, name):
        self.name = name
    # 类的方法
    @classmethod
    def get_apple_to_eve(cls):
        return cls.snake
    
if __name__ == '__main__':
    s = Story('anyone')
    # get_apple_to_eve 是bound方法，查找顺序是先找s的__dict__是否有get_apple_to_eve,如果没有，查类Story
    print(s.get_apple_to_eve)
    # 类和实例都可以使用
    print(s.get_apple_to_eve())
    print(Story.get_apple_to_eve())
    print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)))
    print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)) == s.get_apple_to_eve)


