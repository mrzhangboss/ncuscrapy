# -*- coding: utf-8 -*-
import model
import db_helper
import items
from scrapy.exceptions import DropItem
import logging
import connection
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DropPipeLine(object):
	def process_item(self,item,spider):
		if item['art_url']:
			if db_helper.is_exist_url(item['art_url']):
				raise DropItem('the article had colocted %s' % item['art_url'])
			else:
				return item
		else:
			raise KeyError('the art_url in item should\'n bell null')

class NcuPipeline(object):
    def process_item(self, item, spider):
    	db_helper.save_art(item['art_url'],item['art_type'],item['content'])
    	logging.warning('item saved %s'%item['art_url'])
    	raise DropItem('the article had saved %s'%item['art_url'])

# i = items.NcuItem()
# i['art_url']='www.baidu.com'
# i['art_type']='invitation'
# i['content']='text'
# db_helper.save_art(**i)
