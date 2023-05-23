import requests
key = '64d3bf97-a208-489f-9a6e-84322f5b9afe'


def func(cities):
    res = []
    for city in cities:
        response = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={key}&geocode={city}&format=json')
        json_data = response.json()

        cord = float(json_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']
                     ['pos'].split()[1])
        res.append([city, cord])

    res.sort(key=lambda x: -x[1])
    print(res[-1][0])


cities_list = [i for i in input().split()]
func(cities_list)
