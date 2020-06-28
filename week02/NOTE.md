学习笔记

* Structure of customized exception
  ```python
  class UserError(Exception):
    def __init__(self, ErrorInfo):
      super().__init(self, ErrorInfo)
      self.errorinfo = ErrorInfo
    def __str__(self):
      return self.errorinfo
  
  def test():
    raise UserError('user error')
  ```
  * Deriving from ```Exception```, not ```BaseException``` which is the base class of python build-in exceptions.
  * ```pretty_errors``` lib: display colorful error message
* Methods whose name is surrounded by ```__``` are called **Magic Methods**
* ```del``` keyword is used for freeing memory
* PEP 343 -- The "with" Statement: to factor out ```try/finally``` statements.
  ```python
  class Open:
    def __enter__(self):
      print('open')
    def __exit__(self, type, value, trace):
      print('exit')
    # imitate this class as a function
    def __call__(self):
      pass

  with Open() as f:
    pass
  ```
* ```pymysql``` lib
* anti-crawler
  * user-agent
    * ```fake_useragent``` lib: from fake_useragent import UserAgent
  * cookie
    * ```GET http://httpbin.org/cookies/set/sessioncookie/123456789```
    ```python
    import requests
    def test():
      headers = {}
      data = {}  
      with requests.Session() as s:
          r1 = s.post('http://domain.com', data=data, headers=headers)
          r2 = s.get('http://domain.com/protected')
    ```
  * captcha to text
    * os deps: ```libpng jpeg libtiff leptonica tesseract(ocr)```
    * python deps: ```PIL(Pillow) pytesseract```
    * procedures:
      * gray the image
      * image binaryzation
      * ```pytesseract.image_to_string```
  * proxy IP
    * system proxy
      * ```export http_proxy='http://1.2.3.4:80'```
      * DOWNLOADER_MIDDLEWARES
        * ```scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleWare```
        * To disable a middleware, change priority to None
* How to write a download middleware
  * ```process_request(request, spider)``` order by priority asc
  * ```process_response(request, response, spider)``` order by priority desc
  * ```process_exception(request, exception, spider)```
  * ```from_crawler(cls, crawler)``` must return ```middleware```
* py lib: ```urlparse```
* Distributed crawler
  * scrapy-redis
  * Replace RedisSpider with Spider
  * redis
    * redis.conf
      * bind 127.0.0.1
      * port 6379
      * daemonize yes
    * redis-server redis.conf
    * redis-cli
      * keys *
      * type cluster:items
      * lpop cluster:items
      * keys *
  * ClusterSpider(scrapy.Spider)
    * item['ip'] = json.loads(response.text)['origin']
  * settings.py
    * REDIS_HOST = '127.0.0.1'
    * REDIS_PORT = 6379
    * SCHEDULER = "scrapy_redis.scheduler.Scheduler"
    * DUPEFLITER_CLASS = "scrapy_redis.dupefilder.RFPDupeFliter"
    * SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
    * SCHEDULER_PERSIST = True
    * ITEM_PIPELINES = { ' scrapy_redis.pipelines.RedisPipeline: 300 ' }
  * pipelines.py
    * ScrapyclusterPipeline