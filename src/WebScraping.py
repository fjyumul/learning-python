import requests
from bs4 import BeautifulSoup

url=''
page = requests.get(url).text

# Creates a Beautiful Soup object
soup = BeautifulSoup(page, 'html.parser')

# Pulls all instances of <a> tag
artists = soup.find_all('a')

# Clears data from all tags
for artist in artists:
    names = artist.contents[0]
    fullLink = artist.get('href')
    print(names)
    print(fullLink)