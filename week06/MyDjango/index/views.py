from django.shortcuts import render
from django.http import JsonResponse

from .models import Movie, Comment


def index(request):
  return render(request, 'index.html')


def movies(_request):
  result = Movie.objects.values()
  d = list(result)
  return JsonResponse(d, safe=False)


def search(_request, movie_id, criteria):
  result = Comment.objects.filter(movie_id__exact=movie_id).filter(
    stars__gte=30).filter(txt__icontains=criteria).values()
  d = list(result)
  return JsonResponse(d, safe=False)
