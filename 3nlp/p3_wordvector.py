import numpy as np

# 标量
a = 1
print(a)

# 向量
v1 = np.array([1, 3])
print(v1)
print(v1.shape)

# 矩阵
m1 = np.array([[1, 0], [0, 1]])
print(m1)
print(m1.shape)

# 向量减法
v1 = np.array([1, 0])
v2 = np.array([0, 1])
print(v1 + v2)
v3 = np.array([1, 1])
print(v3 - v1)

# 曼哈顿距离
v1 = np.array([1, 1])
v2 = np.array([2, 2])
from numpy import linalg
print(linalg.norm(v2 - v1, 1))

# 欧几里得距离
print(linalg.norm(v2 - v1, 2))

# 矩阵
m1 = np.array([[1, 2], [2, 3]])
print(m1)
print(m1.shape)

# 矩阵与标量运算
print(m1 + 1)

# 向量的维度(2维)
print(v2.shape)

# 向量的维度(3维)
v3 = np.array([1, 1, 1])
print(v3.shape)

# 矩阵相加
m1 = np.array([[1, 0], [0, 1]])
m2 = np.array([[1, 1], [1, 1]])
print(m1.shape, m2.shape)
print(m1 + m2)

# 矩阵形状不一致会报错
m3 = np.array([[1,], [0,]])
m4 = np.array([[1,], [1,], [2,]])
print(m3.shape, m4.shape)
print(m3 + m4)