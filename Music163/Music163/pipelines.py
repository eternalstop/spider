# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import json
from Music163.MysqlDb import DataBase


class Music163Pipeline(object):
	def __init__(self):
		self.f = open("test.csv", "a+", encoding="utf-8")
		self.db = DataBase()
		self.insert_sql_pre = "insert into sing (songId, name) values "
	
	def process_item(self, item, spider):
		insert_sql = self.insert_sql_pre + item['sql']
		result = self.db.insert(insert_sql)
		playlist_info = '{},{},{},{},{}'.format(item['name'], item['tags'], item['plays'], item['collections'], item['url'])
		self.f.write(playlist_info + '\n')
		self.f.write(insert_sql + '\n')
		self.f.write(result)
		return item

	def close_spider(self, spider):
		self.db.closeDb()
		self.f.close()
