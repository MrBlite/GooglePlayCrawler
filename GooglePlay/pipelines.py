# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.conf import settings

class GoogleplayPipeline(object):

    collection_name = 'AppByCategoryMore_6'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGODB_DBNAME', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        # print('----------------------插入数据')
        return item

    # def __init__(self):
    #     host = settings['MONGODB_HOST']
    #     port = settings['MONGODB_PORT']
    #     dbName = settings['MONGODB_DBNAME']
    #     client = pymongo.MongoClient(host=host, port=port)
    #     tdb = client[dbName]
    #     self.post = tdb[settings['MONGODB_DOCNAME']]
 
    # def process_item(self, item, spider):
    #     AppInfo = dict(item)
    #     self.post.insert(AppInfo)
    #     print('----------------------插入数据')
    #     return item