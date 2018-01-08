class map:
    def __init__(self, data_list):
        self.data_list = data_list
        self.long = []
        self.lat = []
        self.colors = []
        self.text = []

    def map_inputs(self):
        import re
        for tweet in self.data_list:
            self.colors.append(tweet["color"])
            self.long.append(tweet["coordinates"]["coordinates"][0])
            self.lat.append(tweet["coordinates"]["coordinates"][1])
            try:
                self.text.append(re.sub('[^a-zA-Z0-9-_*.]', ' ', re.sub(r"http\S+", ' ', tweet['full_text'])))
            except KeyError:
                self.text.append(re.sub('[^a-zA-Z0-9-_*.]', ' ', re.sub(r"http\S+", ' ', tweet['text'])))
        print(self.text)

    def print_map(self):
        self.map_inputs()

        import gmplot

        # Initialize the map to the first location in the list
        gmap = gmplot.GoogleMapPlotter(self.lat[0], self.long[0], 2)

        # Draw the points on the map. I created my own marker for '#FF66666'.
        # You can use other markers from the available list of markers.
        # Another option is to place your own marker in the folder -
        # /usr/local/lib/python3.5/dist-packages/gmplot/markers/
        gmap.heatmap(self.lat, self.long)
        # for x in range(len(self.data_list)):
        #     gmap.marker(self.lat[x], self.long[x], color=self.colors[x], title=self.text[x])

        gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
        # Write the map in an HTML file
        gmap.draw('map.html')

