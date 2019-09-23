# -*- coding: utf-8 -*-
import scrapy
from Music163.items import Music163Item


class Music163Spider(scrapy.Spider):
    name = 'music163'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/playlist?id=997386069']
    
    def parse(self, response):
        node_list = response.xpath("//ul[@class='f-hide']/li")
        for node in node_list:
            item = Music163Item()
            item['name'] = node.xpath("./a/text()")[0].extract()
            item['song_id'] = node.xpath("./a/@href")[0].extract().split("=")[1]
            yield item
