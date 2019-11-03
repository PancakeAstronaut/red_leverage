from backend import weather
from config import global_key_access


def arb():
    print("not here")


def create_rpt(data):
    weather_type = data[0]
    temp = data[1]
    hasprecip = data[2]
    preciptype = data[3]
    wind = data[4]
    if "Rain" in weather_type:
        hazard_msg = global_key_access.nhtsa_hazards['Rain']
    elif "Storm" in weather_type:
        hazard_msg = global_key_access.nhtsa_hazards['Storm']
    elif "Snow" in weather_type:
        hazard_msg = global_key_access.nhtsa_hazards['Snow']
    elif "Fog" in weather_type:
        hazard_msg = global_key_access.nhtsa_hazards['Fog']
    elif "Clear" in weather_type:
        hazard_msg = global_key_access.nhtsa_hazards['Clear']
    else:
        hazard_msg = "No weather Alerts, Drive Safely!"

    rpt_list = [weather_type, hazard_msg, temp, hasprecip, preciptype, wind]
    return rpt_list


def eval_dest_weather(loc_string):
    cur_weather = weather.get_current(loc_string)
    weather_text = str(cur_weather[0]['WeatherText'])
    has_precip = str(cur_weather[0]['HasPrecipitation'])
    temp = str(cur_weather[0]['Temperature']['Imperial']['Value']) + " " + str(
        cur_weather[0]['Temperature']['Imperial']['Unit'])
    if has_precip:
        precip_type = str(cur_weather[0]['PrecipitationType'])
    else:
        precip_type = "None"
    wind = str(cur_weather[0]['Wind']['Speed']['Imperial']['Value']) + " " + str(
        cur_weather[0]['Wind']['Speed']['Imperial']['Unit'])
    current = [weather_text, temp, has_precip, precip_type, wind]
    return current


def eval_current_loc(loc_string):
    cur_weather = weather.get_current(loc_string)
    weather_text = str(cur_weather[0]['WeatherText'])
    has_precip = str(cur_weather[0]['HasPrecipitation'])
    temp = str(cur_weather[0]['Temperature']['Imperial']['Value']) + " " + str(cur_weather[0]['Temperature']['Imperial']['Unit'])
    if has_precip:
        precip_type = str(cur_weather[0]['PrecipitationType'])
    else:
        precip_type = "None"
    wind = str(cur_weather[0]['Wind']['Speed']['Imperial']['Value']) + " " + str(
        cur_weather[0]['Wind']['Speed']['Imperial']['Unit'])
    current = [weather_text, temp, has_precip, precip_type, wind]
    return current


if __name__ == '__main__':
    # arb()
    x = eval_dest_weather("40.793252%2C%20-77.866309")
    c = create_rpt(x)
    for i in c:
        print(i)
