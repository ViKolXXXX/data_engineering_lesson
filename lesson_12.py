# ДЗ:
# 1. Доделать предыдущее ДЗ - чтобы все пункты работали.
# 2. Попробовать зарегистрироваться на сайте с курсами валют.
# 3. Вместо моего ключа подставить свой - код можно взять у меня в проекте - но лучше напрограммируйте вручную - чтобы запомнить, что делать надо.
# 4. Получить курс рубля к доллару и евро к доллару за каждый день ноября 2023 года - и записать в 1 csv файл в 3 колонки:
# Дата  Валюта  Курс к доллару
from datetime import datetime
import time

import requests
import pandas as pd

class Currency:

    __api_key = '15a7f1474ead9825c1b17e37c52009b4'

    def __init__(self, curr:str):
        if self.__validate_val(curr, str):
            self.curr = curr

    @classmethod
    def __validate_val(cls, val, type_val):  # Валидатор значений
        if isinstance(val, type_val):
            return True

    def get_curr_server_response(self, curs_date):
        # Получаем ответ от сервера валют
        time.sleep(1)  # Требование сервиса 1 запрос 1 в секунду
        curs_date = datetime.strptime(curs_date, "%Y-%m-%d").isoformat()
        URL = (f' https://currate.ru/api/?get=rates&pairs={self.curr}&date={curs_date}&key={self.__api_key}')
        currency_server_response = requests.get(url=URL)
        return currency_server_response

    def parse_server_response_curr(self, currency_server_response, one_curr:str)->str:
        # Получаем числовое значение о валюте, парсим ответ сервера
        result = currency_server_response.json()
        return result.get('data').get(one_curr)



def get_res_dict():
    # Получить курс рубля к доллару и евро к доллару за каждый день ноября 2023 года - и записать в 1 csv файл в 3 колонки
    usdrub_eurrub = Currency('USDRUB,EURRUB')
    data_list = []
    val_USDRUB_list = []
    val_EURRUB_list = []
    for day in range(1, 31): # В ноябре 30 дней
        curs_date = f'2018-11-{day:02}'
        response_server = usdrub_eurrub.get_curr_server_response(curs_date)
        val_USDRUB = usdrub_eurrub.parse_server_response_curr(response_server, 'USDRUB')
        val_EURRUB = usdrub_eurrub.parse_server_response_curr(response_server, 'EURRUB')
        val_USDRUB_list.append(val_USDRUB)
        val_EURRUB_list.append(val_EURRUB)
        data_list.append(curs_date)

    res_dict = {'Дата': data_list, 'USDRUB': val_USDRUB_list, 'EURRUB': val_EURRUB_list}

    return (res_dict)

def tocsv(res_dict, name_file):
    df = pd.DataFrame(res_dict)
    df.to_csv(name_file, index=False)

res_dict = get_res_dict()
name_file_csv = "file_csv.csv" # например name_file.csv
tocsv(res_dict, name_file_csv)
