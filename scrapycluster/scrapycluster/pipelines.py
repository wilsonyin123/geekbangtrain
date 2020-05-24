# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyclusterPipeline:
    def process_item(self, item, spider):
        return item


#  redis 存储了item
#  bash$  redis-cli
#  redis> keys *
#  redis> type cluster:items
#  redis> lpop cluster:items
#  redis> keys *