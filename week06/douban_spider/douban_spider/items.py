# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanSpiderItem(scrapy.Item):
    title = scrapy.Field()
    comment = scrapy.Field()  # Dict(stars, text)
