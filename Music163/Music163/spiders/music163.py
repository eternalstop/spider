# -*- coding: utf-8 -*-
import scrapy
from Music163.items import Music163Item
from Music163.MysqlDb import DataBase


class Music163Spider(scrapy.Spider):
    name = 'music163'
    allowed_domains = ['music.163.com']
    # db = DataBase()
    # select = "SELECT url FROM music163.playlist WHERE ISNULL(collections)"
    # result = db.fetchAll(select)
    # start_urls = [i[0] for i in result]
    # db.closeDb()
    start_urls = ['https://music.163.com/playlist?id=2434603800']
    
    def parse(self, response):
        insert_list = []
        item = Music163Item()
        song_node = response.xpath("//ul[@class='f-hide']/li/a")
        for node in song_node:
            insert_list.append(''.join('("{}", "{}")'.format(node.xpath("./@href").extract()[0].split("=")[1], node.xpath("./text()").extract()[0].replace("(", "\(").replace(")", "\)"))))
        insert_sql = ','.join(insert_list)
        item['sql'] = insert_sql
        item['name'] = response.xpath("//h2/text()")[0].extract()
        item['plays'] = response.xpath("//strong[@id='play-count']/text()")[0].extract()
        item['tags'] = ';'.join(response.xpath("//a[@class='u-tag']/i/text()").extract())
        item['collections'] = response.xpath("//div[@id='content-operation']/a/i/text()")[1].extract().strip('()')
        item['url'] = response.url
        yield item
