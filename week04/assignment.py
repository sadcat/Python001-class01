import pandas as pd
import numpy as np


class PDtoSQL(object):
  def __init__(self):
    self.users = pd.read_csv('users.csv')
    self.orders = pd.read_csv('orders.csv')
    self.orders_2 = pd.read_csv('orders_2.csv')

  def select_all_users(self):
    print(self.users)

  def select_10_users(self):
    print(self.users.head(10))

  def select_id_from_users(self):
    print(self.users[['id']])

  def count_user_ids(self):
    users_count = self.users[['id']].count()
    print(users_count)

  def select_id_less_1k_and_age_greater_30_from_users(self):
    filtered_users = self.users[(self.users['id'] > 1000) & (self.users['age'] < 30)]
    print(filtered_users)

  def select_id_and_count_order_id(self):
    result = self.orders.groupby('user_id').aggregate({'id': 'count', })
    print(result)

  def inner_join_by_id(self):
    merged = self.users.merge(self.orders, left_on='id', right_on='user_id')
    print(merged)

  def union_two(self):
    concated = pd.concat([self.orders, self.orders_2])
    print(concated)

  def delete_id_eql_10_from_users(self):
    new_users = self.users.loc[self.users['id'] != 10]
    print(new_users)

  def alter_column_name(self):
    self.users.rename(columns={'gender': 'sex'}, inplace=True)
    print(self.users)


def main():
  c = PDtoSQL()
  c.alter_column_name()


if __name__ == '__main__':
  main()
