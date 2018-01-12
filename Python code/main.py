from data_collector import DataCollector
datacollector = DataCollector()

while datacollector.interval == 0 or datacollector.number_of_intervals == 0 or datacollector.neutral_tweets == "w":
    try:
        datacollector.interval = float(input("Set interval in minutes: "))
        datacollector.number_of_intervals = int(input("Set number of intervals: "))
        datacollector.neutral_tweets = input("Discard neutral tweets? (Y/N): ")
        if datacollector.neutral_tweets != ("Y" or "N"):
            datacollector.neutral_tweets = "w"
            raise ValueError
    except ValueError:
        print("One of the inputs is not correct, try again")

datacollector.start_collecting()
