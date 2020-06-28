a = 123
b = 123
c = a
print(id(a))
print(id(b))
print(id(c))

a = 456
print(id(a))
c = 789
c = b = a


x = [1,2,3]
y = x
x.append(4)
print(x)
print(y)


a = [1, 2, 3]
b = a
a = [4, 5, 6]
#  a和b分别是什么值？

a = [1, 2, 3]
b = a
a[0],a[1],a[2] = 4, 5, 6
#  a和b分别是什么值？

