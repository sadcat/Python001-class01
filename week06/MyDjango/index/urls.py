from django.urls import path, re_path
from . import views


urlpatterns = [
  path('', views.index),
  path('movies', views.movies),
  path('search/<int:movie_id>/<str:criteria>', views.search),
]
