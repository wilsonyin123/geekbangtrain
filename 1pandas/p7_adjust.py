# 列的选择,多个列要用列表
df[ ['star', 'new_star'] ]

# 某几列
df.iloc[:, [0,2]] # :表示所有行，获得第1和第3列

# 行选择
df.loc[ [0, 2] ] # 选择第1行和第3行
df.loc[ 0:2    ] # 选择第1行到第3行

# 比较
df[ ( df['年龄']<30 ) & ( df['员工id']<100 )   ]


# 数值替换

# 一对一替换
# 用于单个异常值处理
df['年龄'].replace(240,37)

df.replace(np.NaN, 0)

# 多对一替换
df.replace([100,200,300], 1000)

# 多对多替换
df.replace({100:10,200:20,300:30})



# 排序
# 按照指定列降序排列
df.sort_values ( by = ['new_star'] ,ascending = False)

# 多列排序
df.sort_values ( by = ['col1','col2'] ,ascending = [True,False])


# 删除
# 删除列
df.drop( df.columns['a','b'] ,axis = 1)

# 删除行
df.drop(  ['a','b'] ,axis = 0)

# 删除特定行
df [  df['年龄'] <40 ]


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