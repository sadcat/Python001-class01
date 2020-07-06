import pymysql
import db_config


class ConnDB(object):
  def __init__(self):
    self.conn = None

  def open(self):
    self.conn = pymysql.connect(
      host=db_config.host,
      port=db_config.port,
      user=db_config.user,
      password=db_config.password,
      db=db_config.database)

  def execute(self, sqls):
    cur = self.conn.cursor()
    try:
      for command in sqls:
        cur.execute(command)
      cur.close()
      self.conn.commit()
    except Exception as err:
      self.conn.rollback()
      print(err)

  def close(self):
    self.conn.close()
