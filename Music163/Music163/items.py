# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Music163Item(scrapy.Item):
    # define the fields for your item here like:
    song_id = scrapy.Field()
    name = scrapy.Field()
    time = scrapy.Field()
    singer = scrapy.Field()
    album = scrapy.Field()
    composer = scrapy.Field()
    writer = scrapy.Field()
    lyric = scrapy.Field()
    flag = scrapy.Field()



