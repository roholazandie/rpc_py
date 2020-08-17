import requests
import time

for keyword in ["basketball", "atlas", "apollo", "albert einstein", "obama", "yandex", "google", "lulluby"]:
    r = requests.post('http://localhost:8080/wiki',  json={'question': keyword})
    print(r.text)
    #time.sleep(0.5)