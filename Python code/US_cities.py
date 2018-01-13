import csv
import os

class us_cities:
    def __init__(self):
        self.file_name = 'uscities.csv'
        self.root = os.path.abspath(os.path.dirname(__file__))
        self.path = os.path.join(self.root, 'data', self.file_name)

    def load_cities(self):
        with open(self.path , newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cities_dict = {}
            for row in csvreader:
                cities_dict[row[0] + str(", ") + row[1]] = [float(row[3]), float(row[2])]
        return cities_dict

    def save_cities(self, place, coordinates):
        with open(self.path, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|')
            city_state = place.split(", ")
            csvwriter.writerow([city_state[0],city_state[1], coordinates[0], coordinates[1]])




