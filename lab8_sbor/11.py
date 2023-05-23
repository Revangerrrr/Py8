import requests
from bs4 import BeautifulSoup

response = requests.get('http://olympus.realpython.org/profiles')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')

for link in links:
    href = link.get('href')
    print('http://olympus.realpython.org' + href)
