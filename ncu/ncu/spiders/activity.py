# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ncu.coding_patch import encode_content
from ncu.items import NcuItem


class ActivitySpider(CrawlSpider):
    name = 'activity'
    allowed_domains = []
    start_urls = ['http://www.ncu.edu.cn/xxhd/index.html']

    rules = (
        Rule(LinkExtractor(allow=('index[0-9].html',),)),
        Rule(LinkExtractor(allow=r'http://skc.ncu.edu.cn/show.asp\?id=[\d]*'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = NcuItem()
        i['art_url']=response.url
        i['art_type']='news'
        content=response.xpath('//table[@width="770"]').extract()[3]
        i['content']=encode_content(response.encoding,content,response.body)
        print i['content']
        return i
