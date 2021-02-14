import mapinfo
import pygeodesy

class Player:
    def __init__(self, score):
        self.score = score

    def add_score(self, x):
        self.score += x

    def get_score(self):
        return self.score


class Score:
    place = mapinfo.FindPlace()                 #instancitates a random place
    place = place.get_location()
    lat2 = place['lat']
    lon2 = place['lng']

    def distance(lat1, lon1, lat2=place['lat'], lon2=place['lng']):
        '''p = pi / 180
        a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
        return 12742 * asin(sqrt(a))  # 2*R*asin... 20k is the maximum distance that one could be theoretically'''
        return pygeodesy.flatLocal(lat1, lon1, lat2, lon2)
