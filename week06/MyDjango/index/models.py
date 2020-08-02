from django.db import models


class Movie(models.Model):
  title = models.CharField(max_length=256)
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()


class Comment(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  stars = models.IntegerField()
  txt = models.CharField(max_length=8192)
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()
