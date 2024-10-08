# ДЗ:
# 1. Доделать предыдущее ДЗ - чтобы все пункты работали.
# 2. Попробовать зарегистрироваться на сайте с курсами валют.
# 3. Вместо моего ключа подставить свой - код можно взять у меня в проекте - но лучше напрограммируйте вручную - чтобы запомнить, что делать надо.
# 4. Получить курс рубля к доллару и евро к доллару за каждый день ноября 2023 года - и записать в 1 csv файл в 3 колонки:
# Дата  Валюта  Курс к доллару
import time

import requests
import pandas as pd

class Currency:

    __api_key = 'bf1fe2196cf10451b7c562f2d27a486b'

    def get_response_currency_date(self, date_r, source_currencies, currencies):
        # Запрашивем у сервера ответ date_r '2023-02-01' , source_currencies 'USD', currencies 'RUB, EUR'
        URL = (f'https://api.currencylayer.com/historical?access_key={self.__api_key}&date={date_r}&currencies={currencies}&source={source_currencies}&format = 1')
        response_server = requests.get(url=URL)

        return response_server

    def parse_get_currency_date(self, response_server, currency_from_to:str):
        # Получаем числовое значение о валюте

        print(response_server.json())
        result = response_server.json()

        print(result)

        return result.get('quotes').get(currency_from_to)


# class ConvertTOCSV:
#
#
#
#     def pandas_to_csv_file(self, name_file, l=None):


currencies = 'RUB, EUR'
source_currencies = 'USD' # Не работает, только по платной подписке
# date_r = '2023-02-01'
currency_from_to = 'USDRUB'


RubUSD = Currency()

dict_resultat = {}

res_list = []
def res():
    for i in range(1, 31):
        time.sleep(1)
        date_r = f'2023-11-{i:02}'
        print(date_r)
        response_server = RubUSD.get_response_currency_date(date_r, source_currencies, currencies)
        print(response_server)
        val = RubUSD.parse_get_currency_date(response_server, currency_from_to)

        res_list.append(val)
    print(res_list)
res()

#  data = {
# ...    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
# ...    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
# ...             'Manchester', 'Cairo', 'Osaka'],
# ...    'age': [41, 28, 33, 34, 38, 31, 37],
# ...    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
# ... }








