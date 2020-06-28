# GOD
class Human(object):
    def __init__(self, name):
        self.name = name

    # 将方法封装成属性
    @property
    def gender(self):
        return 'M'

h1 = Human('Adam')
h2 = Human('Eve')
h1.gender

# AttributeError:
h2.gender = 'F'



#################
# GOD
class Human2(object):
    def __init__(self):
        self._gender = None
    # 将方法封装成属性
    @property
    def gender2(self):
        print(self._gender)

    # 支持修改
    @gender2.setter
    def gender2(self,value):
        self._gender = value

    # 支持删除
    @gender2.deleter
    def gender2(self):
        del self._gender


h = Human2()
h.gender = 'F'
h.gender
del h.gender
# 另一种property写法
# gender  = property(get_, set_, del_, 'other property')


# 被装饰函数建议使用相同的gender2
# 不使用setter 并不能真正意义上实现无法写入，gender被改名为 _Article__gender



# property 纯python实现

class Property(object):
    "Emulate PyProperty_Type() in Objects/descrobject.c"
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
            self.__doc__ = doc
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)
