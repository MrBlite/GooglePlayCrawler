import scrapy
from scrapy.linkextractors import LinkExtractor
from GooglePlay.items import GoogleplayItem 
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
class AppSpider(CrawlSpider):
    name = "App"
    allowed_domains = ["play.google.com"]
    start_urls = [
        'http://play.google.com/store/apps'
        # 'https://play.google.com/store/apps/details?id=air.net.machinarium.Machinarium.GP'
    ]
 
    rules =( 
        Rule(LinkExtractor(allow=("/store/apps/details", )), callback = 'parse_item', follow = False),
    )
 
    def parse_item(self, response):
        # if response.url.find('reviewId') != -1: return
        item = GoogleplayItem()

        item["name"] = response.css('.AHFaub>span::text').extract()
        item["url"] = response.url
 
        yield item
 