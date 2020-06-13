import pandas as pd
# 行列调整
df = pd.DataFrame({"A":[5,3,None,4], 
                 "B":[None,2,4,3], 
                 "C":[4,3,8,5], 
                 "D":[5,4,2,None]}) 
# 列的选择,多个列要用列表
df[ ['A', 'C'] ]

# 某几列
df.iloc[:, [0,2]] # :表示所有行，获得第1和第3列

# 行选择
df.loc[ [0, 2] ] # 选择第1行和第3行
df.loc[ 0:2    ] # 选择第1行到第3行

# 比较
df[ ( df['A']<5 ) & ( df['C']<4 )   ]


# 数值替换

# 一对一替换
# 用于单个异常值处理
df['C'].replace(4,40)

import numpy as np
df.replace(np.NaN, 0)

# 多对一替换
df.replace([4,5,8], 1000)

# 多对多替换
df.replace({4:400,5:500,8:800})



# 排序
# 按照指定列降序排列
df.sort_values ( by = ['A'] ,ascending = False)

# 多列排序
df.sort_values ( by = ['A','C'] ,ascending = [True,False])


# 删除
# 删除列
df.drop( 'A' ,axis = 1)

# 删除行
df.drop( 3 ,axis = 0)

# 删除特定行
df [  df['A'] < 4 ]


# 行列互换
df.T
df.T.T

# 索引重塑
df4 = pd.DataFrame([
                     ['a', 'b', 'c'], 
                     ['d', 'e', 'f']
                    ],
                    columns= ['one', 'two', 'three'],
                    index = ['first', 'second']
                   )       
df4.stack()
df4.unstack()    
df4.stack().reset_index()             