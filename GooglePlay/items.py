# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoogleplayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    url=scrapy.Field()
    inc=scrapy.Field()
    category=scrapy.Field()
    intro=scrapy.Field()
    reviewNum=scrapy.Field()
    score=scrapy.Field()
    downloadNum=scrapy.Field()
