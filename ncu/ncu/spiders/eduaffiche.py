# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ncu.coding_patch import encode_content
from ncu.items import NcuItem


class EduafficheSpider(CrawlSpider):
    name = 'eduaffiche'
    allowed_domains = ['ncu.edu.cn']
    start_urls = ['http://jwc.ncu.edu.cn/jwtz/index.htm']

    rules = (
        Rule(LinkExtractor(allow=r'[\d]*.htm'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = NcuItem()
        i['art_url']=response.url
        i['art_type']='eduaffiche'
        content=response.xpath('//div[@class="aside"]').extract()[0]
        i['content']=encode_content(response.encoding,content,response.body)
        print i['content']
        return i
