# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FisrtspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()


class HuxiuItem(scrapy.Item):
    """
    虎嗅容器
    """
    url = scrapy.Field() #链接地址
    title = scrapy.Field()#标题
    desc = scrapy.Field()#简介
    posttime = scrapy.Field() #发布时间


class PoxyItem(scrapy.Item):
    '''
    代理容器
    '''
    ip = scrapy.Field()#ip
    duankou = scrapy.Field()#端口
    address = scrapy.Field()#服务器地址
    isniming = scrapy.Field()#是否匿名
    types = scrapy.Field()#类型
    sudu = scrapy.Field()#速度
    connectsudu = scrapy.Field()#连接时间
    livetime = scrapy.Field()#存活时间
    vierytime = scrapy.Field()#验证时间