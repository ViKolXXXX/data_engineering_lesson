# Так это и есть задание после 12 урока - настроить выгрузку информации о курсах валют и о погоде.
# названия валют и названия городов читать из yaml файлов.
from datetime import datetime
import time
import requests
import pandas as pd



URL = 'https://api.gismeteo.net/v2/search/cities/?lang=en&query=москва'
# response = requests.get(url = URL, headers = {'X-Gismeteo-Token: 56b30cb255.3443075'})
respo = requests.get(url=URL)
print(response)