import pandas as pd

# 算数运算
# 两列之间的加减乘除
df['num1'] + df['num2'] 

# 任意一列加/减一个常数值，这一列中的所有值都加/减这个常数值
df['num1'] + 5

# 比较运算
df['num1'] > df ['num2']  

# count非空值计数
excel1 = pd.read_excel(r'0321.xlsx')
excel1.count()
excel1.sum()
df['new_star'].sum()

# mean求均值
# max求最大值
# min求最小值
# median求中位数  
# mode求众数
# var求方差
# std求标准差



