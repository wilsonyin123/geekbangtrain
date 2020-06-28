class Foo(object):
    """类三种方法语法形式"""

    def instance_method(self):
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))

    @staticmethod
    def static_method():
        print("是静态方法")

    @classmethod
    def class_method(cls):
        print("是类方法")

foo = Foo()
foo.instance_method()
foo.static_method()
foo.class_method()
print('----------------')
Foo.static_method()
Foo.class_method()



'''
类方法用在模拟java定义多个构造函数的情况。
由于python类中只能有一个初始化方法，不能按照不同的情况初始化类。
'''
class Book(object):

    def __init__(self, title):
        self.title = title

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        return book

book1 = Book("python")
book2 = Book.create("python and django")
print(book1.title)
print(book2.title)



############
class Fruit(object):
    total = 0

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))

    @classmethod
    def set(cls, value):
        print(f'calling {cls} ,{value}')
        cls.total = value

class Apple(Fruit):
    pass

class Orange(Fruit):
    pass

# >>> Apple.set(100)
# calling <class '__main__.Apple'> ,100
# >>> Orange.set(200)
# calling <class '__main__.Orange'> ,200
# >>> org=Orange()
# >>> org.set(300)
# calling <class '__main__.Orange'> ,300
# >>> Apple.print_total()
# 100
# 140735711069824
# 140735711073024
# >>> Orange.print_total() 
# 300
# 140735711069824
# 1998089714064
# >>>
