import google_streetview.api
import mapinfo
import os


class StreetView():
    def __init__(self):
        self.place = mapinfo.FindPlace()
        self.location = self.place.get_location()
        params = [{
            'size': '600x300',  # max 640x640 pixels
            'location': f"{self.location['lat']}, {self.location['lng']}",
            'key': 'API_KEY'
        }]

        results = google_streetview.api.results(params)

        # Download images to directory 'downloads'
        results.download_links('downloads')


if __name__ == "__main__":
    StreetView()
