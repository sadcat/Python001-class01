import orator


class Comment(orator.Model):
  __table__ = 'soda_comment'


class Product(orator.Model):
  __table__ = 'soda_product'

  @orator.orm.has_many('product_id')
  def comments(self):
    return Comment
