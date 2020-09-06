from django.db import models

# create database smzdm collate utf8mb4_general_ci


class Product(models.Model):
  title = models.CharField(max_length=256)
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()


class Comment(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  content = models.CharField(max_length=8192)
  emotion = models.FloatField()
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()
