import pandas as pd

x = pd.Series([ 1, 2, np.nan, 3, 4, 5, 6, np.nan, 8])
#检验序列中是否存在缺失值
x.hasnans

# 将缺失值填充为平均值
x.fillna(value = x.mean())

# 前向填充缺失值

df3=pd.DataFrame({"A":[5,3,None,4], 
                 "B":[None,2,4,3], 
                 "C":[4,3,8,5], 
                 "D":[5,4,2,None]}) 
                 
df3.isnull().sum() # 查看缺失值汇总
df3.ffill() # 前一行
df3.ffill(axis=1)  # 前一列

# 缺失值删除
excel1 = pd.read_excel(r'0321.xlsx')
excel1.info()
excel1.dropna()

# 填充缺失值
excel1.fillna('无')

# 重复值处理
excel1.drop_duplicates()

# 重新设置行索引
df.set_index=['new_star']