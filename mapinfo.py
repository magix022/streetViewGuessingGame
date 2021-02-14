import pprint
import urllib
from random import randint, uniform

import rand as rand
from bs4 import BeautifulSoup
from requests import request
import googlemaps
import os

longitude_bounds = [-141.00, -52.61]
latitude_bounds = [41.66, 83.11]
types = ['atm',
'bakery',
'bank',
'bar',
'book_store',
'cafe',
'clothing_store',
'convenience_store',
'department_store',
'drugstore',
'electronics_store',
'hospital',
'jewelry_store',
'movie_theater',
'night_club',
'park',
'pharmacy',
'primary_school',
'restaurant',
'secondary_school',
'shoe_store',
'shopping_mall',
'stadium',
'supermarket',
'tourist_attraction',
'university']

class FindPlace():
    def __init__(self):
        self.client = googlemaps.Client(key='API_KEY')
        index = randint(0, len(types) - 1)
        places_result = self.client.places(query=types[index], region='ca', location=[uniform(41.66, 83.11), uniform(-141.00, -52.61)])
        self.res = places_result['results']
        while len(self.res) == 0:
            places_result = self.client.places(query=types[index], region='ca', location=[uniform(41.66, 83.11), uniform(-141.00, -52.61)])
        self.res = places_result['results']
        if "Canada" not in self.res[randint(0, len(self.res) - 1)]:
            self.place = self.res[randint(1, len(self.res) - 1)]
        else:
            self.place = self.res[randint(0, len(self.res) - 1)]
        #pprint.pprint(place)

    def get_location(self):
        return self.place['geometry']['location']

