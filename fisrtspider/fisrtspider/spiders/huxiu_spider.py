#coding:utf-8
__author__ = "langtuteng"
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print sys.path
from fisrtspider.items import HuxiuItem
import scrapy
import logging
class HuxiuSpider(scrapy.Spider):
    '''
    虎嗅爬虫
    '''

    name = "huxiu"
    allowed_domains = ["huxiu.com"]
    start_urls = ["http://www.huxiu.com/index.php"]

    def parse(self, response):
        '''
        解析response
        :param response:
        :return:
        '''
        r1 = response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]')

        for each in r1:
            item = HuxiuItem()
            item['url'] = each.xpath('h2/a/@href')[0].extract()
            url = response.urljoin(item['url'])
            item['title'] = each.xpath('h2/a/text()')[0].extract()
            item['desc'] = each.xpath('div[@class="mob-sub"]/text()')[0].extract()
            item['posttime'] = each.xpath('div[@class="mob-author"]/span/text()')[0].extract()
            # print item['url'],item['title'],item['desc'],item['posttime']
            print url
            yield scrapy.Request(url,callback=self.parse_article)

    def parse_article(self,response):
        print "wwwwwwwwwwwwwwwwwwwwwwwwww"
        detail = response.xpath('//div[@class="article-wrap"]')
        print detail
        item = HuxiuItem()
        item['title'] = detail.xpath('h1/text()')[0].extract()
        item['url'] = response.url
        item['posttime'] = detail.xpath('div[@class="article-author"]/div[@class="column-link-box"]/span[@class="article-time pull-left"]/text()')[0].extract()
        logging.info(item['title'], item['url'], item['posttime'])
        print item['title'], item['url'], item['posttime']
        yield item