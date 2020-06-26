import requests
from bs4 import BeautifulSoup


def find_movies(parsed):
  movies = parsed.find_all('div', attrs={'class': 'movie-item-hover'})
  for movie in movies:
    movie_divs = movie.find_all('div', attrs={'class': 'movie-hover-title'})
    movie_detail_divs = list(movie_divs)
    movie_name = movie_detail_divs[1].get('title')
    type_divs = list(movie_detail_divs[1])
    movie_type = type_divs[2].strip()
    debut_divs = list(movie_detail_divs[3])
    movie_debut = debut_divs[2].strip()
    yield [movie_name, movie_type, movie_debut]


def request_page(url):
  user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) ' \
               'AppleWebKit/537.36 (KHTML, like Gecko) ' \
               'Chrome/78.0.3904.108 Safari/537.36'
  header = {'user-agent': user_agent}
  response = requests.get(url, headers=header)
  return response.text


def main():
  url = 'https://maoyan.com/films?showType=3'
  page_content = request_page(url)
  parsed = BeautifulSoup(page_content, 'html.parser')

  counter = 0
  with open('output.csv', 'w', encoding="utf-8") as file:
    file.write('电影名称,电影类型,上映时间\n')
    for movie in find_movies(parsed):
      if counter >= 10:
        break
      file.write('{name},{movie_type},{debut}\n'.format(
        name=movie[0], movie_type=movie[1], debut=movie[2]))
      counter += 1


if __name__ == '__main__':
  main()
