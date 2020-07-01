import scrapy
from spiders.items import MovieItem

_URL = 'https://maoyan.com/films?showType=3'


class MovieSpider(scrapy.Spider):
  name = 'movie'
  allowed_domains = ['mouyan.com']
  start_urls = [_URL]

  def start_requests(self):
    try:
      yield scrapy.Request(url=_URL, callback=self.parse, dont_filter=False)
    except Exception as ex:
      print(ex)

  def parse(self, response):
    items = []
    divs = response.selector.xpath('//div[@class=\'movie-hover-info\']')
    for div in divs:
      item = MovieItem()
      item['title'] = div.xpath('div[2]/@title').extract_first().strip()
      item['movie_type'] = div.xpath('div[2]/text()[2]').extract_first().strip()
      item['debut'] = div.xpath('div[4]/text()[2]').extract_first().strip()
      items.append(item)
    return items
