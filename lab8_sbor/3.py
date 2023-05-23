import requests
key = '64d3bf97-a208-489f-9a6e-84322f5b9afe'

response = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={key}&geocode=37.617779,55.755246&format=json')
json_data = response.json()

print('Адрес: ', end='')
print(json_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']
      ['GeocoderMetaData']['text'])
print('Координаты: ', end='')
print(json_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'])
