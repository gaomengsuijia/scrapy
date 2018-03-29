# -*- coding: utf-8 -*-
import scrapy
from fisrtspider.items import FisrtspiderItem

class DbcSpider(scrapy.Spider):
    name = 'dbc'
    allowed_domains = ['www.dbc61.com']
    start_urls = ['http://www.dbc61.com/']

    def parse(self, response):
        content = scrapy.selector.Selector(response)
        print content
