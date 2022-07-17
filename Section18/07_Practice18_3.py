import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'

response = requests.get(url)

html = response.text
soup = BeautifulSoup(html,"html.parser")
movie_in_list = soup.find_all('tr')
for movie in movie_in_list:
    if movie.find('img',alt='up') != None:
        print(movie.find('a').text)