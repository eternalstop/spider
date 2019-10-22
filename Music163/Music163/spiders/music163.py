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
            # extract方法将xpath对象转换为Unicode字符串
            item['name'] = node.xpath("./a/text()")[0].extract()
            song_url = node.xpath("./a/@href")[0].extract()
            item['song_id'] = song_url.split("=")[1]
            # 返回每个提取到的Item数据，并交由pipline，pipline处理完之后再返回for循环
            yield item
