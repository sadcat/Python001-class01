from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from .models import Product, Comment


def index(request):
  return render(request, 'index.html')


def result(_request):
  sql = """
  select p.id, title, total_comments,positive_comments,
    round(positive_comments/total_comments*100, 0) as positive_rate
  from soda_product p
inner join (
    select product_id, count(id) as total_comments
    from soda_comment
    group by product_id
    ) c1 on c1.product_id = p.id
inner join (
    select p2.id, ifnull(positive_comments, 0) as positive_comments from soda_product p2
    left join (
        select product_id, count(id) as positive_comments
        from soda_comment
        where emotion > 0.5
        group by product_id
        ) c2 on p2.id = c2.product_id
) c3 on c3.id = p.id;
  """
  with connection.cursor() as cursor:
    cursor.execute(sql)
    rows = cursor.fetchall()

  return JsonResponse(rows, safe=False)
