# 执行批量插入
values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
cursor.executemany('INSERT INTO '+ TABLE_NAME +' values(%s,%s)' ,values)

# 练习
# 1 pymysql是否是线程安全的？如何使用ThreadPoolExecutor与pymysql实现多线程访问数据库
