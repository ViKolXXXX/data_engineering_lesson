# ДЗ.
# 1. Переписать ваш проект с сохранением текущей погоды по городам таким образом, чтобы сохранял файлы в отдельную
# папку. Так же файл должен называться следующем образом: 2024-01-11 23:55:56.csv - где сначала идёт дата,
# потом время - когда сохраняем файл.
# 2. Перенести ваш проект на linux сервер - лучше создать для него отдельную папку.
# 3. Запустить 1 раз его на линуксовом сервере.
# 4. Сделать, чтобы код запускался и создавал файлы раз в час. Для этого использовать cron
# https://1cloud.ru/help/linux/kak-nastroit-planirovshchik-cron-na-crontab-linux
# https://www.youtube.com/watch?v=52-eyCp56ew
import time

import requests
import json
import yaml
from lesson_13 import *
from lesson_12 import *
import sys
sys.path.append("..")
from config.global_config import *
from datetime import datetime
import pandas as pd
import os



class UnloadingLog:

    def __init__(self, source_dictionary):
        self.source_dictionary = source_dictionary

    def to_csv_no_index(self):
        filename = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df = pd.DataFrame(data=self.source_dictionary, columns=['Город', 'Температура'])
        outdir = 'log'
        fullname = os.path.join(os.path.dirname(__file__), outdir)
        if not os.path.exists(fullname):
            os.mkdir(fullname)
        print(df)
        try:
            df.to_csv(f'{fullname}/{filename}.csv', index=False)
        except Exception as e:
            print(f'Ф-ция сохранение в csv файл {e}')

class PogodaOpenWeather(Pogoda):
    __access_key = API_KEY_POGODA_OpenWeather

    def __init__(self):
        pass
    def dict_get_pogoda(self, cities):
        cities_temp = list()
        for city in cities:
            time.sleep(2)
            cities_temp.append([city, self.get_pogoda(city)])
        return cities_temp

    def get_pogoda(self, city):
        coordinates = self._get_coords_city(city)
        lat = float(coordinates['lat']) # Широта
        lon = float(coordinates['lon']) # Долгота
        url = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid="
               f"{self.__access_key}&units=metric")
        print(url)
        try:
            print('Начало запроса')
            response = requests.get(url)
            print(response)

        except ConnectionError as e:
            print(f'Подключение к сервису погоды - {e}')
            exit()
        except Exception as e:
            print(f'Подключение к сервису погоды - {e}')
            exit()

        if response.status_code == 200:
            return round(response.json().get('main').get('temp')) # Возвращаем температуру в Цельсиях
        else:
            return  f'Погоды нет - код ошибки {response.status_code}'

if __name__=='__main__':
    pogoda_city = PogodaOpenWeather()
    pogoda_cities = pogoda_city.dict_get_pogoda(['Пермь', 'Москва', 'Якутск'])
    l = UnloadingLog(pogoda_cities)
    l.to_csv_no_index()



