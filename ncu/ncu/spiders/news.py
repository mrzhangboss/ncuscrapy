# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ncu.coding_patch import encode_content
from ncu.items import NcuItem


class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['ncu.edu.cn']
    start_urls = ['http://news.ncu.edu.cn/html/ndyw/index.html']

    rules = (
        Rule(LinkExtractor(allow=r'/html/[\d]*/\d*-\d*/n[\d]*.html'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = NcuItem()
        i['art_url']=response.url
        i['art_type']='news'
        content=response.xpath('//div[@class="article_show clearfix"]').extract()[0]
        i['content']=encode_content(response.encoding,content,response.body)
        print i['content']
        return i
