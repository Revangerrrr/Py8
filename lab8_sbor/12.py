import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
authors = []

for page in range(1, 11):
    response = requests.get(f'{url}page/{page}')
    soup = BeautifulSoup(response.content, 'html.parser')




