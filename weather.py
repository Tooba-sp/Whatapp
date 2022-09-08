import datetime as dt
import requests
import json
import pywhatkit


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "2b5ac46da58a8e528c94e1ed553b1375"

city_dict = {}

def get_weather(CITY='chicago'):

    try:

        url = f"{BASE_URL}appid={API_KEY}&q={CITY}"
        response = requests.get(url).json()
        response_dict = dict(response)

        temp = response_dict['main']['temp']
        humidity = response_dict['main']['humidity']
        over_cast = response_dict['weather'][0]['main']


        payload = {
            'city': CITY,
            'temp': temp,
            'humidity': humidity,
            'over_cast': over_cast

        }

        city_dict[CITY] = payload

        weather ={
            'cities' : city_dict
        }
        return weather

    except Exception as e:

        print(f"ERROR:{e}")
        return False



