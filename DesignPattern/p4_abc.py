class Father(object):
    def foo(self):
        raise NotImplementedError()
    def bar(self):
        raise NotImplementedError()

class SubClass(Father):
    def foo(self):
        return 'foo() called'

a = SubClass()
a.foo()
a.bar()  # NotImplementedError



################
from abc import ABCMeta, abstractmethod
class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass

c = Concrete() # TypeError