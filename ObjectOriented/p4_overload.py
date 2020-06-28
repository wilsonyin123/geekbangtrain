class  Klass(object):
    def A(self):
        pass
    def A(self,a, b):
        print(f'{a},{b}')


inst = Klass()
# 没有实现重载
inst.A()
 