# Так это и есть задание после 12 урока - настроить выгрузку информации о курсах валют и о погоде.
# названия валют и названия городов читать из yaml файлов.
import requests

class Pogoda:

    __access_key = "09cc2d8a-ad09-4f85-9ebd-0001c32e9170"

    def get_pogoda(self):
        headers = {
            'X-Yandex-Weather-Key': self.__access_key
        }
        moskva = {lat=52.37125&lon=4.89388}
        response = requests.get('https://api.weather.yandex.ru/v2/forecast?lat=52.37125&lon=4.89388', headers=headers)
        return  response


moskva = Pogoda()
print(moskva.get_pogoda().json())