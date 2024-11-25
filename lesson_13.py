# Так это и есть задание после 12 урока - настроить выгрузку информации о курсах валют и о погоде.
# названия валют и названия городов читать из yaml файлов.
import requests
import json
import yaml
from lesson_12 import Currency
import sys
sys.path.append("..")
from config.global_config import *
import os

# Переписанный класс получения курса
class CurrencyYAML(Currency):
    def __init__(self, curr):
        super().__init__(curr = curr)
        self._curr = self.read_file_yaml()

    def read_file_yaml(self):
        outdir = 'config'
        fullname = os.path.join(os.path.dirname(__file__), outdir)
        name_file = f'{fullname}/currency.yaml'
        print(name_file)
        try:
           with open(f'{name_file}') as file:
               read_list = yaml.load(file, Loader=yaml.FullLoader)
               res = {','.join(read_list.values())}
               res = str(res)
               res = res.replace("{", "").replace("}", "").replace("'", "")
               return res
        except Exception as e:
           print(f'{e} Ошибка при открытии yaml файла с валютами')

    def get_one_curr(self, curr):
        data = super().get_currency_value(curs_date='2018-11-01')
        return f'{curr}: {data[curr]}'




class Pogoda:

    __access_key = API_key_pogoda

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
        url = URL_pogoda

        try:
            response = requests.get(url, params=params, headers=headers)
        except ConnectionError as e:
            print(f'Подключение к сервису погоды - {e}')
            exit()
        except Exception as e:
            print(f'Подкючение к сервису погоды')
            exit()

        if response.status_code == 200:
            data = response.json()
            return  data["fact"]["temp"]
        else:
            # Выводим код ошибки
            return  f'Погоды нет - код ошибки {response.status_code}'


    # name_city: 'Москва', 'Пермь' и т.д.
    # Получение погоды, список городов из YAML файла
    def _get_coords_city(self, city):
        outdir = 'config'
        fullname = os.path.join(os.path.dirname(__file__), outdir)
        name_file = f'{fullname}/cities_coords.yaml'
        with open(f'{name_file}') as file:
            read_list = yaml.load(file, Loader=yaml.FullLoader)
            return read_list[city]



if __name__ == '__main__':
    # Получение валюты, список курса из YAML файла
    a = CurrencyYAML('USDRUB,EURRUB,EURGBP')
    print(a.get_one_curr('USDRUB'))
    moskva = Pogoda('Москва')
    perm = Pogoda('Пермь')
    sohi = Pogoda('Сочи')
    yakutck = Pogoda('Якутск')
    print(f'Температура воздуха в {moskva.city} - {moskva.get_pogoda()}')
    print(f'Температура воздуха в {perm.city} - {perm.get_pogoda()}')
    print(f'Температура воздуха в {sohi.city} - {sohi.get_pogoda()}')
    print(f'Температура воздуха в {yakutck.city} - {yakutck.get_pogoda()}')


