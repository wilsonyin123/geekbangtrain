import pandas as pd
import numpy as np

# 聚合
sales = [{'account': 'Jones LLC','type':'a', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co','type':'b',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc','type':'a',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]

df2 = pd.DataFrame(sales)
df2.groupby('type').groups

for a, b in df2.groupby('type'):
    print(a)
    print(b)

# 聚合后再计算
df2.groupby('type').count()
# df2.groupby('Jan').sum()


# 各类型产品的销售数量和销售总额
df2.groupby('type').aggregate( {'type':'count' , 'Feb':'sum' })


group=['x','y','z']
data=pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "salary":np.random.randint(5,50,10),
    "age":np.random.randint(15,50,10)
    })


data.groupby('group').agg('mean')
data.groupby('group').mean().to_dict()
data.groupby('group').transform('mean')

# 数据透视表
pd.pivot_table(data, 
               values='salary', 
               columns='group', 
               index='age', 
               aggfunc='count', 
               margins=True  
            ).reset_index()
