from urllib import response
from bs4 import BeautifulSoup
import requests

def generateNtop(n = 100) :

    MovieL = []
    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    movies = soup.select('td.titleColumn')
    if n > len(movies):
        n = len(movies)
    for index in range(0, n):
        movie_string = movies[index].get_text()
        Movie = ' '.join(movie_string.split()).replace('.', '')
        MovieL.append(Movie[len(str(index))+1:-7])

    return MovieL


def getSuggestion(genre = 'action'):
    url = f'https://www.imdb.com/search/title/?genres={genre}&title_type=feature'
    response = requests.get(url)
    soup = BeautifulSoup(response.text , "html.parser")
    movies = soup.select('h3.lister-item-header')

    li = []


    for index in range(0, len(movies)):
        movie_string = movies[index].get_text()
        movie = ' '.join(movie_string.split()).replace('.','')
        movie_title = movie[len(str(index))+1:-7]
        li.append(movie_title)

    return li
    
