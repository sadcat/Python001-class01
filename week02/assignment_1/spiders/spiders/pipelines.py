# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from . import db_helper


class SpidersPipeline:
    def process_item(self, item, spider):
        host = spider.settings.get("MYSQL_HOST")
        port = spider.settings.get("MYSQL_PORT")
        user = spider.settings.get("MYSQL_USER")
        password = spider.settings.get("MYSQL_PASSWORD")
        db_name = spider.settings.get("MYSQL_DB")
        db_instance = db_helper.DBHelper(host, port, user, password, db_name)
        sql = 'INSERT INTO movies(?,?,?) VALUES (\'{title}\', \'{movie_title}\', \'{debut}\')'.format(
            title=item['title'],
            movie_type=item['movie_title'],
            debut=item['debut'])
        db_instance.execute(sql)

        return item
