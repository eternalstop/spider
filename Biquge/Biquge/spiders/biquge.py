# -*- coding: utf-8 -*-
import scrapy


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['www.5atxt.com']
    start_urls = ['http://www.5atxt.com/']

    def parse(self, response):

        """
        章节名称：//h1/text()
        正文：//div[@id='content']/text()
        下一章：//a[@class='next']/@href
        :param response:
        :return:
        """
        pass
