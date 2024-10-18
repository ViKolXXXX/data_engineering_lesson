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



# Получение валюты с сайта currate.ru.
# Инициализация например 'USDRUB,EURRUB'. На выходе словарь {'USDRUB': '65.8644', 'EURRUB': '74.5241'}
class Currency:

    __api_key = '15a7f1474ead9825c1b17e37c52009b4'

    def __init__(self, curr):
        self._curr = curr

    @property
    def curr(self):
        return self._curr
    @curr.setter
    def curr(self, curr):
        if isinstance(curr, str):
            self._curr = curr
        else:
            raise ValueError

    # Получаем значение валют
    def get_currency_value (self, curs_date='2018-11-01') -> {}:
        time.sleep(1)  # Требование сервиса 1 запрос 1 в секунду
        curs_date = datetime.strptime(curs_date, "%Y-%m-%d").isoformat()
        URL = (f' https://currate.ru/api/?get=rates&pairs={self._curr}&date={curs_date}&key={self.__api_key}')

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

# Выгрузка словаря в CSV
class Unloading:

    def __init__(self, source_dictionary):
        self.__source_dictionary = source_dictionary

    @property
    def source_dictionary(self):
        return self.__source_dictionary
    @source_dictionary.setter
    def source_dictionary(self, curr):
        if isinstance(__source_dictionary, dict):
            self.__source_dictionary = source_dictionary
        else:
            raise ValueError

    # Выгрузка словаря в CSV без индекса
    def to_csv_no_index(self, file_name):
        df = pd.DataFrame(self.__source_dictionary)
        df.to_csv(file_name, index=False)

    def to_csv_index(self, file_name):
        df = pd.DataFrame(data = self.__source_dictionary)
        df.to_csv(file_name, index=True)
        print(df)

def dz_lesson12():

    usdrub_eurrub = Currency('USDRUB,EURRUB,EURGBP')
    data_list = []
    val_USDRUB_list = []
    val_EURRUB_list = []
    val_EURGBP_list = []
    for day in range(1, 5):  # В ноябре 30 дней
        curs_date = f'2018-11-{day:02}'
        response_server = usdrub_eurrub.get_currency_value(curs_date)
        print(response_server)
        val_USDRUB = response_server.get('USDRUB')
        val_EURRUB = response_server.get('EURRUB')
        val_EURGBP = response_server.get('EURGBP')
        val_USDRUB_list.append(val_USDRUB)
        val_EURRUB_list.append(val_EURRUB)
        val_EURGBP_list.append(val_EURGBP)
        data_list.append(curs_date)

    res_dict = {'Дата': data_list, 'USDRUB': val_USDRUB_list, 'EURRUB': val_EURRUB_list, 'EURGBP': val_EURGBP}

    result = Unloading(res_dict)

    result.to_csv_index(file_name="test4.csv")

    return (res_dict)


if __name__ == '__main__':
    print(dz_lesson12())

# print(dz_lesson12())

