import pandas as pd
import numpy as np

dates = pd.date_range('20200101', periods=12)
df = pd.DataFrame(np.random.randn(12,4), index=dates, columns=list('ABCD'))
df

#                    A         B         C         D
# 2020-01-01  0.046485 -0.556209  1.062881 -1.174129
# 2020-01-02  1.066051 -0.343081  1.054913  1.601051
# 2020-01-03  0.191064 -0.386905  0.516403  0.259818
# 2020-01-04 -0.168462 -1.488041 -0.457658  0.913574
# 2020-01-05 -0.502614  1.235633 -0.578284 -0.362737
# 2020-01-06 -0.193310  0.652285 -0.346359  0.347364
# 2020-01-07  2.308562 -0.679108  0.856449  0.490840
# 2020-01-08  0.871489  0.338133 -0.163669  0.300147
# 2020-01-09 -1.245250  0.667357 -1.287782  1.494880
# 2020-01-10  0.387925 -1.058867 -0.397298  0.514921
# 2020-01-11 -0.440884  0.904307  1.338720  0.612919
# 2020-01-12 -0.864941 -0.358934 -0.203868 -1.191186

import matplotlib.pyplot as plt
plt.plot(df.index, df['A'], )
plt.show()

plt.plot(df.index, df['A'], 
        color='#FFAA00',    # 颜色
        linestyle='--',     # 线条样式
        linewidth=3,        # 线条宽度
        marker='D')         # 点标记

plt.show()

# seaborn其实是在matplotlib的基础上进行了更高级的API封装，从而使绘图更容易、更美观
import seaborn as sns
# 绘制散点图
plt.scatter(df.index, df['A'])
plt.show()

# 美化plt
sns.set_style('darkgrid')
plt.scatter(df.index, df['A'])
plt.show()
