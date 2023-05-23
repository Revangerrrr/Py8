import requests

response = requests.get('https://static-maps.yandex.ru/1.x/?ll=86.927486,54.565762&spn=3,3&l=map'
                        '&pl=86.086088,55.397158,86.188123,54.674655,87.154984,53.794622,87.945098,52.962816')

with open('C:/Users/Пользователь/Desktop/Pyhton/lab8_sbor/8.png', 'wb') as file:
    file.write(response.content)
