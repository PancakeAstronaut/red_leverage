import googlemaps as mapdata
from googlemaps import directions
from config import global_key_access
import geocoder
import reverse_geocoder
from itertools import islice
from collections import OrderedDict

# Declare Google maps object using the API key from Google Cloud
rawGmapdata = mapdata.Client(key=global_key_access.MAPS_API_KEY)


def get_current_location():     # grabs the users current location
    # gets the current location according to system IP address
    loc = geocoder.ip('me')
    latitude = loc.lat
    longitude = loc.lng
    coordinates = (latitude, longitude)
    # searches for the address location with lat/long
    loc_list = reverse_geocoder.search(coordinates)
    loc_dict = OrderedDict(loc_list[0])
    slice_loc_list = islice(loc_dict.items(), 7)
    # making a list out of an ordered dictionary
    newList = list(slice_loc_list)
    # slicing though the list to get data
    cur_city = newList[2][1]
    cur_state = newList[3][1]
    cur_county = newList[4][1]
    cur_nation = newList[5][1]
    # building coordinates that accuweather can use
    # weatherCoord = str(latitude) + "%2C%20" + str(longitude)
    ctyState = str(cur_city) + ", " + str(cur_state)
    location = [ctyState, cur_county, cur_nation]
    return location


def arb():          # arbitrary placeholder function
    print("not supposed to be here")


def get_Distances(start, finish):           # gets distances from JSON return
    data = directions.directions(rawGmapdata, start, finish)
    # slicing through JSON response for specific data
    distance_string = data[0]['legs'][0]['distance']['text']
    dist_meters = data[0]['legs'][0]['distance']['value']
    # building a list of related distance value [string, integer]
    distances = [distance_string, dist_meters]
    return distances


def get_Coordinates(start, finish):         # gets coordinates from JSON return
    data = directions.directions(rawGmapdata, start, finish)
    # slicing through JSON response for specific data
    start_coordinates = str(data[0]['legs'][0]['start_location']['lat']) + "%2C%20" + str(data[0]['legs'][0]['start_location']['lng'])
    end_coordinates = str(data[0]['legs'][0]['end_location']['lat']) + "%2C%20" + str(data[0]['legs'][0]['end_location']['lng'])
    # building a list of related distance value [string, string]
    coordinates = [start_coordinates, end_coordinates]
    return coordinates


def get_Addresses(start, finish):           # gets addresses from JSON response
    data = directions.directions(rawGmapdata, start, finish)
    # slicing through JSON response for specific data
    start_address = data[0]['legs'][0]['start_address']
    end_address = data[0]['legs'][0]['end_address']
    # building a list of related distance value [string, string]
    addresses = [start_address, end_address]
    return addresses


def get_Duration(start, finish):            # gets duration of trip from JSON response
    data = directions.directions(rawGmapdata, start, finish)
    # slicing through JSON response for specific data
    duration_txt = data[0]['legs'][0]['duration']['text']
    duration_val = data[0]['legs'][0]['duration']['value']
    # building a list of related distance value [string, integer]
    duration = [duration_txt, duration_val]
    return duration


if __name__ == '__main__':
    arb()
