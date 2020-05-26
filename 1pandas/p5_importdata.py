import pandas as pd
# pip install xlrd
# 导入excel文件
excel1 = pd.read_excel(r'0321.xlsx')
excel1
# 指定导入哪个Sheet
pd.read_excel(r'0321.xlsx',sheet_name = 0)

# 指定第2行做列索引
# head参数值默认为0，即用第一行作为列索引
pd.read_excel(r'0321.xlsx',head = 1)


# 支持其他常见类型
pd.read_csv(r'c:\file.csv',sep=' ', nrow=10, encoding='utf-8')

pd.read_table( r'file.txt' , sep = ' ')

import pymysql
sql  =  'SELECT *  FROM mytable'
conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
df = pd.read_sql(sql,conn)


# 熟悉数据
# 显示前几行
excel1.head(3)

# 行列数量
excel1.shape

# 详细信息
df.info()
df.describe()