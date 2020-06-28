'''编写高质量代码  建议7
无论采用哪一种方式来实现常量，都提倡将常量集中到一个文件中，
因为这样有利于维护，一旦需要修改常量的值，可以集中统一进行而不是逐个文件去检查。
采用第二种方式实现的常量可以这么做：
将存放常量的文件命名为constant.py，并在其中定义一系列常量'''

class _const:

    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError(f"Can't change const.{name}")
        if not name.isupper():
            raise self.ConstCaseError(f"const name {name} is not all uppercase")
        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()



const = _const()
const.A = 'B'
const.Ab = 'B'
const.Ab = 'B'


# 其他文件
# from constant import const
const.A = 'B'