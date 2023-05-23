import requests
from bs4 import BeautifulSoup
import random

url = 'https://quotes.toscrape.com/'
all_quotes = []

for page in range(1, 11):
    response = requests.get(f'{url}page/{page}')
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all(class_='quote')
    for quote in quotes:
        all_quotes.append({quote.find(class_='text').get_text()})

for i in range(5):
    quote = random.choice(all_quotes)
    print(quote)
