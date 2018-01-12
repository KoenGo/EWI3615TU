from data_collector import DataCollector
datacollector = DataCollector()

while datacollector.interval == 0 or datacollector.number_of_intervals == 0:
    try:
        datacollector.interval = float(input("Set interval in minutes: "))
        datacollector.number_of_intervals = int(input("Set number of intervals: "))
    except ValueError:
        print("One of the inputs is not a number, try again")

datacollector.start_collecting()
