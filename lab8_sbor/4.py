import requests
key = '64d3bf97-a208-489f-9a6e-84322f5b9afe'

response1 = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={key}&geocode=Барнаул&format=json')
response2 = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={key}&geocode=Мелеуз&format=json')
response3 = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={key}&geocode=Йошкар-Ола&format=json')

json_data1 = response1.json()
json_data2 = response2.json()
json_data3 = response3.json()

print('Барнаул: ', end='')
print(json_data1['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']
      ['GeocoderMetaData']['Address']['Components'][2]['name'])

print('Мелеуз: ', end='')
print(json_data2['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']
      ['GeocoderMetaData']['Address']['Components'][2]['name'])

print('Йошкар-ола: ', end='')
print(json_data3['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']
      ['GeocoderMetaData']['Address']['Components'][2]['name'])
