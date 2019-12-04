# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BiqugePipeline(object):
    def __init__(self):
        self.f = open('C:\\Users\\A-Li\\Documents\\Downloads\\Biquge\\biquge.txt', "a+", encoding="utf-8")

    def process_item(self, item, spider):
        self.f.write(item['eve_title'])
        for content in item['eve_content']:
            self.f.write(content.strip() + "\n")
        self.f.write("\n\n")
        return item

    def close_spider(self, spider):
        self.f.close()
