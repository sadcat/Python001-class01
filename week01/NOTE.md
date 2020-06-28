#### Note

* requests lib: a http request lib that is more convenient than the built-in urllib2 lib.
* bs4 lib: BeautifulSoup lib is a collection parser that structures html string. It's slow.
* lxml lib: python wrapper of a C implemented xpath parser
  ```python
  import lxml.etree
  def test():
    html = '<html><head></head><body>content</body></html>'
    selector = lxml.etree.HTML(html)
    txt = selector.xpath('//@text()[1]')
    print(txt)
  ```
* yield and generator
* list comprehension ```[i for i in range(1, 10) if i%2==0]```
* Scrapy: A web crawl framework
  * a scrapy project contains multiple crawlers. ```scrapy startproject project_name```
  * creation of crawler by executing ```scrapy genspider spider_name domain.com```
  * parsing logic ```parse(response)``` is in ```spider_name.py```
  * captured items are processed in ```pipeline.py```
    * must return item or DropItemException is thrown.
  * useful configurations in ```settings.py```
    * USER_AGENT
    * DOWNLOAD_DELAY
    * ITEM_PIPELINES, need to be enabled or funcs in ```pipeline.py``` won't be called  
  * Debugging
    ```python
    import scrapy
    
    # Ignore allow_domains
    def start_requests(self):
      scrapy.Request(url="http://domain.com", callback=self.parse, dont_filter=True)
    ```
  * ```items.py```
    * defining new model class by inheriting ```scrapy.Item```
    * add field ```field_name = scrapy.Field()``` 
  * ```selector```, selecting elems by xpath
    * ```new_selector = response.selector.xpath(xpath_code)```
    * ```another_selector = new_selector.xpath(xpath_code)```
    * ```val = another_selector.extract_first()```
    * ```vals = another_selector.extract()```
    