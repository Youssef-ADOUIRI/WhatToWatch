import re
from bs4 import BeautifulSoup
import requests
from scraping import db_man


def generateNtop(n = 100) :

    MovieL = []
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
        year = ''
        search = re.search('\((.*?)\)', movie_string)
        if (search):
            year = search.group(0)
        place = Movie[:len(str(index))-(len(Movie))]
        data = {"_id": index,
            "place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            "star_cast": crew[index],
            }
        MovieL.append(data)
        
    
    db_man.insert(MovieL)
    

    return MovieL


def getSuggestions(genres='action'):
    url = 'https://www.imdb.com/search/title/?title_type=feature&genres='+ genres
    response = requests.get(url)
    soup = BeautifulSoup(response.text , "html.parser")
    movies = soup.select('h3.lister-item-header')
    movie_section = soup.select('p.text-muted')
    photos_html = soup.select('img.loadlate')
    li = []

    for index in range(0, len(movies)):
        movie_string = movies[index].get_text()
        movie = ' '.join(movie_string.split()).replace('.','')
        movie_title = movie[len(str(index))+1:-7]
        # search for the description and the photo refrence
        year = ''
        search = re.search('\((.*?)\)', movie_string)
        if (search):
            year = search.group(0)
        description = movie_section[2*index+1].get_text()
        #image_url_low = photos_html[index].get('loadlate')
        #firstUrl = image_url_low.split('@')
        #image_url_high = firstUrl[0] + '@' + '._V1_QL75_UY562_CR516,0,380,562_.jpg'
        image_id = photos_html[index].get('data-tconst')
        data = {"title" : movie_title + ' ' + year,
            "description" : description,
            "image_id" : image_id }
        li.append(data)

    return li

def get_imageURL_fromID(img_id):
    #scrap the the image from the movie name
    url = 'https://www.imdb.com/title/' + str(img_id)
    response = requests.get(url)
    soup = BeautifulSoup(response.text , "html.parser")
    image_url = soup.select('img.ipc-image')
    return image_url[0].get('src')

def get_top_movies(n):
    docs= db_man.findAll(lim=n)
    #temporary function ( may god help me remember to remove it )
    print('docs : ')
    print(docs)

    Li = []
    for s in docs:
        output_str = '{} - {} ({})'.format(s['place'] , s['movie_title'] ,s['year'])
        Li.append(output_str)
        print('appended : '+ output_str)
    
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