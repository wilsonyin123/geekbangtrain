# 使用type元类创建类
def hi():
    print('Hi metaclass')

# type的三个参数:类名、父类的元组、类的成员
Foo = type('Foo',(),{'say_hi':hi})
foo = Foo
foo.say_hi()




def pop_value(self,dict_value):
    for key in self.keys():
        if self.__getitem__(key) == dict_value:
            self.pop(key)
            break
    
class DelValue(type):
    def __new__(cls,name,bases,attrs):
        attrs['pop_value'] = pop_value
        return type.__new__(cls,name,bases,attrs)
 
class DelDictValue(dict,metaclass=DelValue):
    # python2的用法，在python3不支持
    # __metaclass__ = DelValue
    pass

d = DelDictValue()
d['a']='A'
d['b']='B'
d['c']='C'
d.pop_value('C')
for k,v in d.items():
    print(k,v)
 