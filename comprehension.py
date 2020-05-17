mylist = []
for i in range(1, 11):
    if i > 5:
        mylist.append(i**2)

# 列表推导式
mylist2 = [i**2 for i in range(1, 11) if i > 5]

# 循环嵌套
mylist = [str(i) + j for i in range(1, 6) for j in 'ABCDE']

# 用推导式将字典转换为列表
mydict = {'key1': 'value1', 'key2': 'value2'}
mylist2 = [key + ':' + value for key, value in mydict.items()]

# 推导式生成字典
mydict = {i: i*i for i in (5, 6, 7)}

# 推导式实现字典的k-v互换
{value: key for key, value in mydict.items()}

# 推导式生成集合
myset = {i for i in 'HarryPotter' if i not in 'er'}

# 推导式生成 生成器
mygenerator = (i for i in range(0, 11))
print(mygenerator)
print(list(mygenerator))