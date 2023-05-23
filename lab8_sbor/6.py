import requests

response = requests.get('https://static-maps.yandex.ru/1.x/?ll=133.795384,-25.694768&spn=20,20&l=sat')

with open('C:/Users/Пользователь/Desktop/Pyhton/lab8_sbor/6.png', 'wb') as file:
    file.write(response.content)
