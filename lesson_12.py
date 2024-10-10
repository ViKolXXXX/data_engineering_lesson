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

    def __init__(self, curr: str):
        if self.__validate_val(curr, str):
            self.curr = curr

    @classmethod
    def __validate_val(cls, val, type_val):  # Валидатор значений
        if isinstance(val, type_val):
            return True

    # Получаем значение валют
    def get_currency_value (self, curs_date='2018-11-01') -> {}:
        time.sleep(1)  # Требование сервиса 1 запрос 1 в секунду
        curs_date = datetime.strptime(curs_date, "%Y-%m-%d").isoformat()
        URL = (f' https://currate.ru/api/?get=rates&pairs={self.curr}&date={curs_date}&key={self.__api_key}')

        try:
            currency_server_response = requests.get(url=URL)
        except requests.ConnectionError as e:
            print("Ошибка подключения:", e)
            exit()
        except requests.Timeout as e:
            print("Ошибка тайм-аута:", e)
            exit()
        except requests.RequestException as e:
            print("Ошибка запроса:", e)
            exit()

        currency_value =  currency_server_response.json()

        return currency_value.get('data')








    #     l_curr = self.curr.split(",")  # Строку преобразовываем в список
    #
    #     print()
    #     print()
    #
    #     cur_val = dict()
    #     for cur in l_curr:
    #         self._parse_server_response_curr(currency_server_response, cur)
    #         cur_val[cur] =
    #
    #
    # # Получаем числовое значение о валюте, парсим ответ сервера
    # def _parse_server_response_curr(self, currency_server_response, currency) -> str:
    #     try:
    #         currency_json = currency_server_response.json()
    #         val_currency = currency_json.get('data').get(currency)
    #         return val_currency
    #     except:
    #         print('Ошибка в распарсивание данных')
    #         exit()





usdrub_eurrub = Currency('USDRUB,EURRUB')

print(usdrub_eurrub.get_currency_value())
print(type(usdrub_eurrub.get_currency_value()))


#
# def get_res_dict():
#     # Получить курс рубля к доллару и евро к доллару за каждый день ноября 2023 года - и записать в 1 csv файл в 3 колонки
#     usdrub_eurrub = Currency('USDRUB,EURRUB')
#     data_list = []
#     val_USDRUB_list = []
#     val_EURRUB_list = []
#     for day in range(1, 31):  # В ноябре 30 дней
#         curs_date = f'2018-11-{day:02}'
#         response_server = usdrub_eurrub.get_curr_server_response(curs_date)
#         val_USDRUB = usdrub_eurrub.parse_server_response_curr(response_server, 'USDRUB')
#         val_EURRUB = usdrub_eurrub.parse_server_response_curr(response_server, 'EURRUB')
#         val_USDRUB_list.append(val_USDRUB)
#         val_EURRUB_list.append(val_EURRUB)
#         data_list.append(curs_date)
#
#     res_dict = {'Дата': data_list, 'USDRUB': val_USDRUB_list, 'EURRUB': val_EURRUB_list}
#
#     return (res_dict)
#
#
# def tocsv(res_dict, name_file):
#     df = pd.DataFrame(res_dict)
#     df.to_csv(name_file, index=False)
#
#
# res_dict = get_res_dict()
# name_file_csv = "file_csv.csv"  # например name_file.csv
# tocsv(res_dict, name_file_csv)
