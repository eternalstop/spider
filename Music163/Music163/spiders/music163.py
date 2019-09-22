# -*- coding: utf-8 -*-
import scrapy


class Music163Spider(scrapy.Spider):
    name = 'music163'
    allowed_domains = ['https://music.163.com']
    start_urls = ['https://music.163.com/']

    def parse(self, response):
        pass
