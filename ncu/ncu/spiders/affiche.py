# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ncu.items import NcuItem
from ncu.coding_patch import encode_content

class AfficheSpider(CrawlSpider):
    name = 'affiche'
    allowed_domains = []
    start_urls = ['http://www.ncu.edu.cn/xxgg/index.html']

    rules = (
        Rule(LinkExtractor(allow=('index[0-9].html',),)),
        Rule(LinkExtractor(allow=(r'http://cgzx.ncu.edu.cn/zbgg/hwl/[0-9]*.htm',),),callback='parse_cgzx_item',),
        Rule(LinkExtractor(allow=(r'http://yjsy.ncu.edu.cn/yjs_showmsg.asp\?id=[0-9]*',)),callback='parse_yjsy_item'),
        Rule(LinkExtractor(allow=('http://jwc.ncu.edu.cn/jwtz/[0-9]*.htm',),),callback='parse_jwc_item',),
        Rule(LinkExtractor(allow=('http://rsc.ncu.edu.cn/zpxx/(xwzp|xnzp)/[0-9]*.htm',),),callback='parse_rsc_item',),
        Rule(LinkExtractor(allow=('http://cdgh.ncu.edu.cn/gygk/gggsl/[0-9]*.htm',),),callback='parse_cdgh_item',),
        Rule(LinkExtractor(allow=('[0-9]*.html',),),callback='parse_www_item',),
            )



    def parse_cgzx_item(self, response):
        # response.encoding='gbk'
        i = NcuItem()
        i['art_url']=response.url
        i['art_type']='invitation'
        content=response.xpath('//div[@id="article_right"]').extract()[0]
        i['content']=encode_content(response.encoding,content,response.body)
        print i['content']
        return i
    def parse_yjsy_item(self,response):
        i = NcuItem()
        i['art_url']=response.url
        i['art_type']='graduate'
        content=response.xpath('//table[@class="border"]').extract()[0]
        i['content']=encode_content(response.encoding,content,response.body)
        return i
    def parse_jwc_item(self,response):
        i = NcuItem()
        i['art_url']=response.url
        i['art_type']='purchasing'
        content=response.xpath('//div[@class="box3"]').extract()[0]
        i['content']=encode_content(response.encoding,content,response.body)
        print i['content']
        return i
    def parse_rsc_item(self,response):
        i = NcuItem()
        i['art_url']=response.url
        i['art_type']='recruit'
        content=response.xpath('//div[@class="asided"]').extract()[0]
        i['content']=encode_content(response.encoding,content,response.body)
        print i['content']
        return i
    def parse_cdgh_item(self,response):
        i = NcuItem()
        i['art_url']=response.url
        i['art_type']='labor_union'
        content=response.xpath('//td[@style="BACKGROUND-COLOR: #ffffff"]').extract()[0]
        i['content']=encode_content(response.encoding,content,response.body)
        print i['content']
        return i
    def parse_www_item(self,response):
        i = NcuItem()
        i['art_url']=response.url
        i['art_type']='affiche'
        content=response.xpath('//div[@class="w p30 maincontent"]').extract()[0]
        i['content']=encode_content(response.encoding,content,response.body)
        print i['content']
        return i



