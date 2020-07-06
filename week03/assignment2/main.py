import requests
import lxml.etree
import conn
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import time


headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8,zh-CN;q=0.7,zh;q=0.6,zh-TW;q=0.5,en-GB;q=0.4',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}


def get_page(url):
  try:
    time.sleep(3)
    with requests.session() as s:
      s.headers.update(headers)
      r = s.get(url)
      return r.content.decode('utf-8')
  except Exception as err:
    print(err)
    return ""


def parse_page(city, html):
  pos_list = []
  sel = lxml.etree.HTML(html)
  lis = sel.xpath('//li[@class=\'con_list_item default_list\']')
  for li in lis:
    company = li.xpath('@data-company')[0]
    pos_name = li.xpath('@data-positionname')[0]
    salary = li.xpath('@data-salary')[0]
    pos_list.append(
      dict(city=city, company=company, pos_name=pos_name, salary=salary))
  return pos_list


def gen_sqls(pos_list):
  sqls = []
  for d in pos_list:
    city = d['city']
    company = d['company']
    pos_name = d['pos_name']
    salary = d['salary']
    sql = f"insert into positions values(null, \'{city}\',\'{company}\',\'{pos_name}\',\'{salary}\')"
    sqls.append(sql)
  return sqls


def gen_urls():
  urls = dict(BJ='https://www.lagou.com/beijing-zhaopin/Python/'
              , SH='https://www.lagou.com/shanghai-zhaopin/Python/'
              , GZ='https://www.lagou.com/guangzhou-zhaopin/Python/'
              , SZ='https://www.lagou.com/shenzhen-zhaopin/Python/')
  for city in urls.keys():
    url = urls[city]
    for page in range(1, 8):
      yield url+str(page), city


def run():
  url_generator = gen_urls()
  with ThreadPoolExecutor(max_workers=4) as executor:
    futures = dict()
    for page_tuple in url_generator:
      url = page_tuple[0]
      city = page_tuple[1]
      future = executor.submit(get_page, url)
      futures[future] = (url, city)

  try:
    db = conn.ConnDB()
    db.open()
    for f in concurrent.futures.as_completed(futures):
      tup = futures[f]
      html = f.result()
      pos_list = parse_page(tup[1], html)
      sqls = gen_sqls(pos_list)
      db.execute(sqls)
      print(f'processed: {tup[0]}')
  finally:
    db.close()


def main():
  run()


if __name__ == '__main__':
  main()
