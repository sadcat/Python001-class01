import json
import re

import scrapy
from scrapy.selector import Selector
from nest.items import ProductItem

class SodaSpider(scrapy.Spider):
    name = 'soda'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/xifahufa/h5c4s0f0t0p1/#feed-main/']

    def start_requests(self):
        url = self.start_urls[0]
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        products = Selector(response=response).xpath(
            '//a[contains(@class, "z-highlight")]')

        for p in products[0:10]:
            on_click = p.xpath('@onclick').extract_first()
            product_json = re.sub('(dataLayer\\.push\\()|(\\)$)|"', '', on_click)
            product_json = re.sub('\'', '"', product_json)
            product_dict = json.loads(product_json)
            item = ProductItem()
            item['title'] = product_dict['pagetitle']
            item['comments'] = set()
            product_detail_url = p.xpath('@href').extract_first()
            yield scrapy.Request(url=product_detail_url, meta={'item': item}, callback=self.parse2, dont_filter=False)

    def parse2(self, response):
        item = response.meta['item']

        comments = Selector(response=response).xpath(
            "//span[@itemprop='description']")
        for comment in comments:
            c = comment.xpath('text()').extract_first().strip()
            if len(c) != 0:
                item['comments'].add(c)

        next_page = Selector(response=response).xpath(
            '(//ul[@class="pagination"])[1]/li[@class="pagedown"]/a')
        if len(next_page) == 0:
            yield item
        else:
            url = next_page.xpath('@href').extract_first()
            yield scrapy.Request(url=url, meta={'item': item},
                                 callback=self.parse2,
                                 dont_filter=False)
