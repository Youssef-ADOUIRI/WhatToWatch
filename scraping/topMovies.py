import re
from bs4 import BeautifulSoup
import requests
from scraping import db_man


def generateNtop(n = 100) :

    MovieL = []
    MovieT = []
    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    movies = soup.select('td.titleColumn')
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]
    if n > len(movies):
        n = len(movies)
    for index in range(0, n):
        movie_string = movies[index].get_text()
        Movie = ' '.join(movie_string.split()).replace('.', '')
        movie_title = Movie[len(str(index))+1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = Movie[:len(str(index))-(len(Movie))]
        data = {"_id": index,
            "place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            "star_cast": crew[index],
            }
        MovieL.append(data)
        MovieT.append(data['movie_title'])
    
    #db_man.insert(MovieL)
    

    return MovieT


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
    
def get_top_movies(n):
    docs= db_man.findAll(lim=n)
    Li = []
    for s in docs:
        output_str = '{} - {} ({})'.format(s['place'] , s['movie_title'] ,s['year'])
        Li.append(output_str)
    return Li


'''
def generate_movies_list_toDB(genre):
    #get the number of movies in this categorie
    url = f'https://www.imdb.com/search/title/?genres={genre}&title_type=feature'
    response = requests.get(url)
    soup = BeautifulSoup(response.text , "html.parser")

    tot_number = 
    for i_page in range():
        url = f'https://www.imdb.com/search/title/?genres={genre}&title_type=feature&start={}'
'''