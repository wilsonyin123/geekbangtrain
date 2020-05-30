# 1 Python是一门简洁的语言

int temp = var1 ;
var1 = var2 ;
var2 = temp ;

var2, var1 = var1, var2


# 2 所有语言的开头 Hello world
print('Hello, World')

# 3 Python可交互可字节码
>>> x = 1
>>> help(x)
>>> dir()
>>> exit()

# 4 内置数据类型
数值 布尔
字符串
列表、元组、字典、集合

# 4.1 数值常见有 整数、浮点数、复数、布尔值
整数  1 -5 100 8888   
整数没有大小限制，受限于内存

浮点数   2.5 4.8

复数 1+2j 5.6+7.8j

布尔  True 、 False

数值支持算数运算  + - * /  //整数除法 %求模 **求幂

支持数学函数
import math
math.pow(2, 3)

# 4.2 字符串 string
'a'
"a"
'''a'''
"""a"""

# 4.3 列表 list
[]
x = [1, 'a', 'A']
列表可以通过下标访问
x[0]
x[-1]
Python支持对列表的内置函数 len max min
也支持列表本身的方法 append count extend index insert pop remove reverse sort
len(x)
x.reverse()
还支持操作符 in + *
参考： 官方文档-教程

# 4.4 元组 tuple
元组和列表类似，但是一旦被创建就不可修改， 支持操作符 、内置函数 
本身的方法只能支持两个 count index
可以显式转换
y = tuple(x)
z = list(y)
type(z)

# 4.5 字典 dict
字典本质是哈希表，key只能是数值、字符串、元组
dict1 = {'a':1, 'b':2}
本身的方法支持copy、get、items、keys、values、update

# 4.6 集合 set
由基本对象组成的无序集，特点：唯一性
set1 = set([1, 2, 3, 4, 5, 3, 2, 1])
print(set1)

# 5 流程控制
False 0  零值None 空(列表、字典、字符串等) 表示假值
True 其他值  表示真值

# 5.1 if
x = 1
if x < 10:
    y = 1
elif x > 10:
    y = 2
else:
    y = 3
z = 4
代码块与缩进


# 5.2 while  (支持break continue)
x = 2
y = 1
while x > y :
    pass

# 5.3 for  (支持break continue)
for i in z:
    print(i)

# 6 函数
def func1(x, y):
    return x + y

print(func1(10, 20))

# 7 面向对象
class DemoClassName:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y

demo = DemoClassName(10, 20)
print(demo.add())

# 8 标准库的引入
import datetime
datetime.date.today()
from datetime import date
date.today()
