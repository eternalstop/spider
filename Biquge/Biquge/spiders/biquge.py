# -*- coding: utf-8 -*-
import scrapy
from Biquge.items import BiqugeItem


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['www.5atxt.com']
    start_urls = ['https://www.5atxt.com/16_16049/11611760.html']

    def parse(self, response):

        """
        小说名称：//div[@class='con_top']/a/text()
        章节名称：//h1/text()
        正文：//div[@id='content']/text()
        下一章：//a[@class='next']/@href
        :param response:
        :return:
        """

        item = BiqugeItem()
        item["name"] = response.xpath("//div[@class='con_top']/a/text()")[1].extract()
        item["eve_title"] = response.xpath("//h1/text()")[0].extract()
        # item["eve_content"] = "".join(response.xpath("//div[@id='content']/text()").extract())
        item["eve_content"] = response.xpath("//div[@id='content']/text()").extract()
        yield item

        if response.xpath("//a[@class='next']/@href")[0].extract().endswith("html"):
            next_href = "https://www.5atxt.com" + response.xpath("//a[@class='next']/@href")[0].extract()
            yield scrapy.Request(next_href, callback=self.parse)
