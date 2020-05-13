######## 表结构 ##########
CREATE TABLE `article` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL COMMENT '文章标题',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=116 DEFAULT CHARSET=utf8mb4


######## settings.py ##########
#mysql-config
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'scrapy'
MYSQL_USER = 'root'
MYSQL_PASSWD ='rootroot'
MYSQL_PORT = 3306



######## pipelines.py ##########
# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from logging import Logger
from twisted.enterprise import adbapi
from blogscrapy.db.dbhelper import DBHelper
import codecs
from logging import log
from scrapy.utils.project import get_project_settings
class BlogscrapyPipeline(object):
    def __init__(self):
        self.file = open('blog.json', 'a+', encoding='utf-8')
        self.db = DBHelper()
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        self.db.insert(item)
        return item
    def close_spider(self, spider):
        self.file.close()



######## DBHelper.py ##########
# -*- coding: utf-8 -*-
import pymysql
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings
class DBHelper():
    def __init__(self):
        settings = get_project_settings()
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8mb4', 
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        # 将字典扩展为关键字参数
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self.__dbpool = dbpool

    def connect(self):
        return self.__dbpool

    def insert(self, item):
        # 封装insert操作
        sql = "insert into article(title) values(%s)"
        query = self.__dbpool.runInteraction(self._conditional_insert, sql, item)
        query.addErrback(self._handle_error)
        return item

    def _conditional_insert(self, canshu, sql, item):
        # 传items的数据
        params = (item['title'])
        canshu.execute(sql, params)
    def _handle_error(self, failue):
        print(failue)
    def __del__(self):
        try:
            self.__dbpool.close()
        except Exception as ex:
            print(ex)
