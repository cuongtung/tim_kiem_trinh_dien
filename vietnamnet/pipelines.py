# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
# def


from scrapy.exceptions import DropItem
import json


class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['url'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['url'])
            return item


class NoneFilterPipeline(object):

    def process_item(self, item, spider):
        if item['title'] is not None and item['content'] is not None and item['time'] is not None:
            if len(item['title']) == 0 or len(item['content']) == 0 or len(item['time']) == 0:
                raise DropItem('item not valid')
            else:
                return item
        else:
            raise DropItem('item not valid')


class WriteJsonPipeline(object):
    def open_spider(self, spider):
        self.file = open('vietnamnet.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
