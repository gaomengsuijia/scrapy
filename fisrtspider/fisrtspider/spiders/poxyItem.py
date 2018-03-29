#coding:utf-8
__author__ = "langtuteng"
import scrapy
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fisrtspider.items import PoxyItem

class PoxySpider(scrapy.Spider):
    name = "poxy"
    start_urls = ["http://www.xicidaili.com"]
    allowed_domains = ["xicidaili.com"]

    def parse(self, response):
        '''
        获取page
        :param response:
        :return:
        '''
        print "==================================="
        for page in range(2):
            full_url = "http://www.xicidaili.com/nn/%s"%str(page)
            yield scrapy.Request(url=full_url,callback=self.parse_ip)


    def parse_ip(self,response):
        '''
        解析ip
        :param response:
        :return:
        '''
        res = response.xpath('//div[@id="ip_list"]/tbody/tr')
        for each in range(1,len(res)):
            lis = res[each].xpath('th/test()').extract()
            item = PoxyItem()
            item['ip'] = lis[1]
            item['duankou'] = lis[2]
            item['address'] = lis[3]
            item['isniming'] = lis[4]
            item['types'] = lis[5]
            item['sudu'] = lis[6]
            item['connectsudu'] = lis[7]
            item['livetime'] = lis[8]
            item['vierytime'] = lis[9]
            print item['ip'],item['duankou'],item['address'],item['isniming'],item['types'],item['sudu'],\
                item['connectsudu'],item['livetime'],item['vierytime']

            return item