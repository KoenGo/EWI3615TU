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
        import re
        import time
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
                self.text.append(re.sub('[^a-zA-Z0-9-_*.]', ' ', re.sub(r"http\S+", ' ', tweet['full_text'])))
            except KeyError:
                self.text.append(re.sub('[^a-zA-Z0-9-_*.]', ' ', re.sub(r"http\S+", ' ', tweet['text'])))
        for tweet in remove_list:
            self.data_list.remove(tweet)



    def geocode_to_lat_long(self, tweet):
        import time
        import gmplot
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
                    succes = True
                except IndexError:
                    tried_count += 1
        return coordinates

    def print_map(self):
        import gmplot

        self.map_inputs()

        gmap = gmplot.GoogleMapPlotter(self.lat[0], self.long[0], 2)
        for x in range(len(self.data_list)):
            gmap.marker(self.lat[x], self.long[x], color=self.colors[x], title=self.text[x])

        gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
        # Write the map in an HTML file
        gmap.draw('map.html')