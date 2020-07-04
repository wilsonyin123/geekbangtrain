class Foo(object):
    """类三种方法语法形式"""

    def instance_method(self):
        print("是类的实例方法，只能被实例对象调用")

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



import requests