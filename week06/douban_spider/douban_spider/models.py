import orator


class Comment(orator.Model):
  __table__ = 'index_comment'


class Movie(orator.Model):
  __table__ = 'index_movie'

  @orator.orm.has_many('movie_id')
  def comments(self):
    return Comment
