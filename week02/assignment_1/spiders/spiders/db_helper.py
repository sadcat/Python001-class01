import pymysql


class DBHelper(object):
  def __init__(self, host, port, user, password, db_name):
    self.host = host
    self.port = port
    self.user = user
    self.password = password
    self.db_name = db_name

  def execute(self, sql):
    conn = None
    cur = None
    try:
      conn = pymysql.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             password=self.password,
                             db=self.db)
      cur = conn.cursor()
      cur.execute(sql)
      cur.close()
      conn.commit()
    except Exception as err:
      if conn is not None:
        conn.rollback()
      print(err)
    finally:
      if cur is not None:
        cur.close()
      if conn is not None:
        conn.close()
