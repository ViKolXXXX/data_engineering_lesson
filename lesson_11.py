from textwrap import indent
import csv
import yaml
from pandas import DataFrame
from yaml import FullLoader
import json

import pandas as pd

# ДЗ:
# 1. Почитать про YAML формат: https://ru.wikipedia.org/wiki/YAML
# 2. Почитать про JSON формат: https://habr.com/ru/articles/554274/
# 3. Создать класс, в классе хранить лист словарей (как у меня в коде пример с подключениями - можете придумать что-нибудь своё, например в словарях данные людей будут или ещё что-нибудь)
# 4. Сделать 2 метода для работы с YAML - для сохранения в файл и для чтения из файла. Название фала должно передаваться в метод входным параметром.
# 5. Сделать 2 метода для работы с JSON - для сохранения в файл и для чтения из файла. Название фала должно передаваться в метод входным параметром.
# 6. В другом поле хранить Pandas DataFrame с данными. Написать ещё 2 метода - для сохранения данных в файл .csv и для чтения данных из .csv файла в датафрейм.
# Так же написать для 4, 5, 6 пунктов методы, которые будут просто отображать данные, которые внутри объекта хранятся.
# 7. Попробовать при помощи объекта класса прочитать данные из YAML формата, а сохранить - в JSON.
# 8. Наоборот: прочитать данные из JSON, сохранить в YAML.

class Format:

    __things = {'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300,
              'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200,
              'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250}

    __connection = [
        {
            "user_name" : "etl_user",
            "password" : "123123"
        },
        {
            "user_name": "sfaef",
            "password": "00000000"
        }
    ]

    # YAML
    def save_file_yaml(self, name_file):
        with open(f'{name_file}', 'w', encoding="utf-8") as file:
          yaml.dump(self.__connection, file, allow_unicode=True)

    def read_file_yaml(self, name_file):
        with open(f'{name_file}') as file:
            read_list = yaml.load(file, Loader=yaml.FullLoader)
            # print(read_list)
            return read_list

    # JSON
    def save_file_json(self, name_file):
        with open(f'{name_file}', 'w', encoding="utf-8") as outfile:
            json.dump(self.__connection, outfile, ensure_ascii=False, indent=4)

    def read_file_json(self, name_file):
        with open(f'{name_file}') as openfile:
            read_list = json_object = json.load(openfile)
            return  read_list

    # CSV
    def load_pandas(self, l=None):
        if l is None:
            l = self.__connection
        df1 = pd.DataFrame(l)
        return df1  

    def pandas_to_csv_file(self, name_file, l=None):
        df = self.load_pandas(l)
        df.to_csv(name_file, index=False)

    def read_csv(self, name_file):
        df2 = pd.read_csv(name_file)
        return df2

    # JSON to CSV and CSV to JSON
    def json_to_csv(self, name_json_file, name_csv_file):
        json_file = self.read_file_json(name_json_file)
        print(json_file)
        df1 = self.load_pandas(l=json_file)
        df1.to_csv(name_csv_file, index=False)



    def csv_to_json(self, name_csv_file, name_json_file):
        l_csv = self.read_csv(name_csv_file)
        l_csv.to_json(name_json_file, orient='records', lines=True)

object_class_format = Format()

name_file_yaml = "file_yaml.yaml" # например name_file.yaml
name_file_json = "file_json.json" # например name_file.json
name_file_csv = "file_csv.csv" # например name_file.json
new_name_file_csv = "new_name_file_csv.csv" # например name_file.json
new_name_file_json = "new_name_file_json.json" # например name_file.json


object_class_format.save_file_yaml(name_file_yaml)
list_yaml = object_class_format.read_file_yaml(name_file_yaml)
print(list_yaml)
print("________________________________________________________")
object_class_format.save_file_json(name_file_json)
list_json = object_class_format.read_file_json(name_file_json)
print(list_json)
print("________________________________________________________")
print(object_class_format.load_pandas())
object_class_format.pandas_to_csv_file(name_file_csv)
print(object_class_format.read_csv(name_file_csv))
print("________________________________________________________")

object_class_format.json_to_csv(name_file_json, new_name_file_csv)
object_class_format.csv_to_json('from_pandas.csv', new_name_file_json)





