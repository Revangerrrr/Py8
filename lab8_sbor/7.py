import requests

response = requests.get('https://static-maps.yandex.ru/1.x/?ll=86.086848,55.355200&spn=0.05,0.05&'
                        'l=map&pt=86.060110,55.344206~86.125683,55.388649~86.071729,55.375501~86.128322,55.342181')

with open('C:/Users/Пользователь/Desktop/Pyhton/lab8_sbor/7.png', 'wb') as file:
    file.write(response.content)
