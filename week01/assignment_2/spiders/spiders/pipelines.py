# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpidersPipeline:
    def process_item(self, item, spider):
        with open('oupput.csv', 'a+', encoding='utf-8') as file:
            line = "{title},{movie_type},{debut}\n".format(
                title=item['title'],
                movie_type=item['movie_title'],
                debut=item['debut'])
            file.write(line)
        return item
