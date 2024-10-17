# Так это и есть задание после 12 урока - настроить выгрузку информации о курсах валют и о погоде.
# названия валют и названия городов читать из yaml файлов.
import requests
import json
import yaml
from lesson_12 import Currency




a = Currency('USDRUB,EURRUB,EURGBP')
print(a.get_currency_value())



class Pogoda:

    __access_key = "09cc2d8a-ad09-4f85-9ebd-0001c32e9170"
    def __init__(self, city):
        self.city = city

    def get_pogoda(self):

        headers = {
            'X-Yandex-Weather-Key': self.__access_key
        }
        coordinates = self._get_coords_city(self.city)
        lat = float(coordinates['lat']) # Широта
        lon = float(coordinates['lon']) # Долгота

        params = {
            'lat': lat,
            'lon': lon,
            'lang': 'ru_RU'
        }
        url = 'https://api.weather.yandex.ru/v2/forecast'

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return  data["fact"]["temp"]
        else:
            # Выводим код ошибки
            return  response.status_code


    # name_city: 'Москва', 'Пермь' и т.д.
    def _get_coords_city(self, city):

        name_file = 'cities_coords.yaml'
        with open(f'{name_file}') as file:
            read_list = yaml.load(file, Loader=yaml.FullLoader)
            return read_list[city]

moskva = Pogoda('Москва')
perm = Pogoda('Пермь')
sohi = Pogoda('Сочи')
yakutck = Pogoda('Якутск')
print(f'Температура воздуха в {moskva.city} - {moskva.get_pogoda()}')
print(f'Температура воздуха в {perm.city} - {perm.get_pogoda()}')
print(f'Температура воздуха в {sohi.city} - {sohi.get_pogoda()}')
print(f'Температура воздуха в {yakutck.city} - {yakutck.get_pogoda()}')


