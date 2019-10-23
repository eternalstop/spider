# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class Music163Pipeline(object):
	def __init__(self):
		self.f = open("test.csv", "a+")
	
	def process_item(self, item, spider):
		playlist_info = '{},{},{},{}'.format(item['name'], item['tags'], item['plays'], item['collections'])
		self.f.write(playlist_info + '\n')
		return item

	def close_spider(self, spider):
		self.f.close()
