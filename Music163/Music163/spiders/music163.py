# -*- coding: utf-8 -*-
import scrapy
from Music163.items import Music163Item
import pymysql


class Music163Spider(scrapy.Spider):
    name = 'music163'
    allowed_domains = ['music.163.com']
    db = pymysql.connect(host="localhost", user="root", passwd="Missy@u777", db="music163", charset="utf8")
    cursor = db.cursor()
    select = "SELECT url FROM music163.playlist WHERE ISNULL(collections)"
    cursor.execute(select)
    result = cursor.fetchall()
    start_urls = [i[0] for i in result]
    db.close()
    # start_urls = ['https://music.163.com/playlist?id=2434603800']
    
    def parse(self, response):
        item = Music163Item()
        item['name'] = response.xpath("//h2/text()")[0].extract()
        item['plays'] = response.xpath("//strong[@id='play-count']/text()")[0].extract()
        item['tags'] = ';'.join(response.xpath("//a[@class='u-tag']/i/text()").extract())
        item['collections'] = response.xpath("//div[@id='content-operation']/a/i/text()")[1].extract().strip('()')
        item['url'] = response.url
        yield item
