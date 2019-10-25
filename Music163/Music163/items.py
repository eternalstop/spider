# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Music163Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    plays = scrapy.Field()
    tags = scrapy.Field()
    collections = scrapy.Field()
    url = scrapy.Field()
    sql = scrapy.Field()



