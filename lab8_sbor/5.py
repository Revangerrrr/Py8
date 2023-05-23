import requests
key = '64d3bf97-a208-489f-9a6e-84322f5b9afe'
adr = 'Москва,%20Петровки,%2038&'

response = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={key}&geocode={adr}&format=json')
json_data = response.json()

print('Индекс: ', end='')
print(json_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']
      ['GeocoderMetaData']['Address']['postal_code'])
