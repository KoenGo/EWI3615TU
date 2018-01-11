class us_cities:
    def load_cities(self, file_name='uscities.csv'):
        import csv
        import os
        root = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(root, 'data', file_name)
        with open(path , newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            cities_dict = {}
            for row in csvreader:
                if row[0] == 'city':
                    continue
                cities_dict[row[1] + str(", ") + row[2]] = [float(row[8]), float(row[7])]
        return cities_dict
