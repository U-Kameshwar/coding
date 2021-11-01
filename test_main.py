import requests
import datetime
import time

while True:
    print(datetime.datetime.utcnow())
    req = requests.get('https://api.weather.gov/points/39.7456,-97.0892')
    print(req.json())
    time.sleep(10)

