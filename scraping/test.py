import re
from bs4 import BeautifulSoup
import requests

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
        print(movie_string)
        year = ''
        search = re.search('\((.*?)\)', movie_string)
        if (search):
            year = search.group(0)
        description = movie_section[2*index+1].get_text()
        image_url_low = photos_html[1].get('loadlate')
        image_url_high = (image_url_low.split('@'))[0] + '@' + '._V1_QL75_UY562_CR516,0,380,562_.jpg'
        data = {"title" : movie_title + ' ' + year,
            "description" : description,
            "image_url" : image_url_low }
        li.append(data)

    return li
    

l = getSuggestions('adventure')
