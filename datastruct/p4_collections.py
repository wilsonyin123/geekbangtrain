from collections import Counter
mystring = ['a','b','c','d','d','d','d','c','c','e']
# 取得频率最高的前三个值
cnt = Counter(mystring)
cnt.most_common(3)
cnt['b']

# 命名元组
from collections import namedtuple
Point = namedtuple('Ponit', ['x','y'])
p = Point(10, y=20)
p.x + p.y
p[0] + p[1]
x, y = p

# 双向队列
from collections import deque
d = deque('uvw')
d.append('xyz')
d.appendleft('rst')



