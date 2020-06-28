
class Foo(object):
    # 用与方法返回
    def __str__(self):
        return '__str__ is called'

    # 用于字典操作
    def __getitem__(self, key):
        print(f'__getitem__ {key}') 
    
    def __setitem__(self, key, value):
        print(f'__setitem__ {key}, {value}')
    
    def __delitem__(self, key):
        print(f'__delitem__ {key}')

    # 用于迭代
    def __iter__(self):
        return iter([i for i in range(5)])


# __str__
bar = Foo()
print(bar)

# __XXitem__
bar['key1']
bar['key1']='value1'
del bar['key1']

# __iter__
for i in bar:
    print(i)
