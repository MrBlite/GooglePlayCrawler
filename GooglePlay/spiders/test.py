import scrapy
from scrapy.linkextractors import LinkExtractor
from GooglePlay.items import GoogleplayItem 
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
import re

class AppSpider(CrawlSpider):
    name = "App"
    allowed_domains = ["play.google.com"]
    start_urls = [
        'http://play.google.com/store/apps'
        # 'https://play.google.com/store/apps/details?id=air.net.machinarium.Machinarium.GP'
        # 'https://play.google.com/store/apps/details?id=com.hasbro.mlpcoreAPPSTORE'
    ]
 
    rules =( 
        Rule(LinkExtractor(allow=("/store/apps/details", )), callback = 'parse_item', follow = True),
    )
 
    def parse_item(self, response):
        # if response.url.find('reviewId') != -1: return
        item = GoogleplayItem()
        item["name"] = response.css('.AHFaub>span::text').extract_first()
        item["url"] = response.url
        grp = response.css('.T32cc>a::text').extract()
        # print(grp)
        item["inc"] = grp[0]
        item["category"] = grp[1:]
        item["intro"] = response.css('.PHBdkd > div > content > div::text').extract_first()
        reviewNum = response.css('.EymY4b > span::text').extract_first()
        reviewNum=re.sub(r'\D', '', reviewNum)
        item["reviewNum"] = reviewNum
        item["score"] = response.css('.BHMmbe::text').extract_first()
        item["downloadNum"] = response.css('div.hAyfc:nth-child(3) > span:nth-child(2) > div:nth-child(1) > span:nth-child(1)::text').extract_first()
 
        yield item
 