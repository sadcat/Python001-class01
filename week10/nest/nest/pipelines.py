from itemadapter import ItemAdapter
import orator
from snownlp import SnowNLP
from nest.models import Product
from nest.models import Comment


class NestPipeline:
    def __init__(self, db_config):
        self.db_config = db_config

    @classmethod
    def from_crawler(cls, crawler):
        config = {
            'mysql': {
                'driver': 'mysql',
                'host': crawler.settings.get('MYSQL_HOST'),
                'database': crawler.settings.get('MYSQL_DB'),
                'user': crawler.settings.get('MYSQL_USER'),
                'password': crawler.settings.get('MYSQL_PASSWORD'),
            }
        }
        return cls(
            db_config=config
        )

    def open_spider(self, spider):
        db = orator.DatabaseManager(self.db_config)
        orator.Model.set_connection_resolver(db)

    def process_item(self, item, spider):
        product = Product.where('title', '=', item['title']).get().first()
        if product is None:
            product = Product()
            product.title = item['title']
            product.save()

        for comment in item['comments']:
            db_comment = Comment()
            db_comment.product_id = product.id
            try:
                s = SnowNLP(comment)
                db_comment.emotion = s.sentiments
            except Exception as err:
                print(err)
            db_comment.content = comment
            db_comment.save()

        return item
