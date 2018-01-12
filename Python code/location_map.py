import re
import time
import gmplot
from US_cities import us_cities
class map:
    def __init__(self, data_list, cities_dict):
        self.data_list = data_list
        self.long = []
        self.lat = []
        self.colors = []
        self.text = []
        self.remove_tweet = False
        self.cities_dict = cities_dict

    def map_inputs(self):
        remove_list = []
        for tweet in self.data_list:
            self.colors.append(tweet["color"])
            if tweet["coordinates"] is None:
                coordinates = self.geocode_to_lat_long(tweet)
                if coordinates == [0, 0]:
                    remove_list.append(tweet)
                    self.colors.pop()
                    continue
                self.lat.append(coordinates[0])
                self.long.append(coordinates[1])
                time.sleep(0.001)
            else:
                self.long.append(tweet["coordinates"]["coordinates"][0])
                self.lat.append(tweet["coordinates"]["coordinates"][1])
            try:
                normal_text = re.sub(r"http\S+", ' ', tweet['full_text'])
                self.text.append(re.sub(r"[^\w]+", ' ', normal_text))
            except KeyError:
                normal_text = re.sub(r"http\S+", ' ', tweet['text'])
                self.text.append(re.sub(r"[^\w]+", ' ', normal_text))
        for tweet in remove_list:
            self.data_list.remove(tweet)



    def geocode_to_lat_long(self, tweet):
        gmmap = gmplot.GoogleMapPlotter
        tried_count = 0
        place_name = tweet["place"]["full_name"]
        succes = False
        while succes == False:
            if tried_count > 4:
                self.remove_tweet = True
                return [0, 0]
            if tried_count > 1:
                time.sleep(1)
            if place_name in self.cities_dict.keys():
                coordinates = self.cities_dict[place_name]
                succes = True
            else:
                try:
                    coordinates = gmmap.geocode(place_name)
                    us_cities().save_cities(place_name, coordinates)
                    self.cities_dict = us_cities().load_cities()
                    succes = True
                except IndexError:
                    tried_count += 1
                except ConnectionError:
                    self.remove_tweet = True
                    return [0, 0]
        return coordinates

    def print_map(self):
        print(len(self.data_list))
        self.map_inputs()

        gmap = gmplot.GoogleMapPlotter(self.lat[0], self.long[0], 2)
        for x in range(len(self.data_list)):
            gmap.marker(self.lat[x], self.long[x], color=self.colors[x], title=self.text[x])

        gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
        # Write the map in an HTML file
        gmap.draw('map.html')
