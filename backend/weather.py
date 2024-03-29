import requests
import json
from config import global_key_access

apikey = global_key_access.WEATHER_API_KEY

location_base_string = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search"
current_base_string = "http://dataservice.accuweather.com/currentconditions/v1/"
forecast_base_string = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/"


def arb():
    print("You shouldn't be here")


def set_location(query):
    requestString = "{}?apikey={}&q={}".format(location_base_string, apikey, query)
    response = requests.get(requestString)
    location_dict = json.loads(response.text)
    location_keyval = location_dict.get("Key")
    return location_keyval


def get_forecast(query):
    location_keyval = set_location(query)
    requestString = "{}{}?apikey={}&details=true".format(forecast_base_string, location_keyval, apikey)
    response = requests.get(requestString)
    forecast_dict = json.loads(response.text)
    return forecast_dict


def get_current(query):
    location_keyval = set_location(query)
    requestString = "{}{}?apikey={}&details=true".format(current_base_string, location_keyval, apikey)
    response = requests.get(requestString)
    current_dict = json.loads(response.text)
    return current_dict


if __name__ == '__main__':
    arb()

