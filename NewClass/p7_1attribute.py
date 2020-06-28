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
h2.name
# 删除实例属性
del h1.name

# AttributeError
# 访问不存在的属性
h1.name


# __getattribute__ 的底层原理是描述器
class Desc(object):
    """
    通过打印来展示描述器的访问流程
    """
    def __init__(self, name):
        self.name= name
    
    def __get__(self, instance, owner):
        print(f'__get__{instance} { owner}')
        return self.name

    def __set__(self, instance, value):
        print(f'__set__{instance} {value}')
        self.name = value

    def __delete__(self, instance):
        print(f'__delete__{instance}')
        del self.name

class MyObj(object):
    a = Desc('aaa')
    b = Desc('bbb')

if __name__ == '__main__':
    inst = MyObj()
    print(inst.a)
    inst.a = 456
    print(inst.a)


# __getattribute__ 纯python实现
def __getattribute__(self, key):
    "Emulate type_getattro() in Objects/typeobject.c"
    v = object.__getattribute__(self, key)
    if hasattr(v, '__get__'):
      return v.__get__(None, self)
    return v