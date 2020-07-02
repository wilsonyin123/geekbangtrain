1、Django安装
2、Django目录结构
3、URL规则
4、view视图
5、模型与数据库
6、模板

常见报错
1  django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 'MySQLdb'
解决方法：在 __init__.py 文件中添加以下代码即可
import pymysql
pymysql.install_as_MySQLdb()

2   version = Database.version_info
# if version < (1, 3, 13):
# raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)

3  AttributeError: 'str' object has no attribute 'decode'
出现这个错误之后可以根据错误提示找到文件位置，打开 operations.py 文件，找到以下代码：
def last_executed_query(self, cursor, sql, params):
    query = getattr(cursor, '_executed', None)
    # if query is not None:
    #     query = query.decode(errors='replace')
    return query