from data_collector import DataCollector
datacollector = DataCollector()

while datacollector.interval == 0 or datacollector.number_of_intervals == 0 or datacollector.remove_neutral_tweets == "w":
    try:
        datacollector.interval = float(input("Set interval in minutes: "))
        datacollector.number_of_intervals = int(input("Set number of intervals: "))
        datacollector.remove_neutral_tweets = input("Discard neutral tweets? (Y/N): ").lower()
        if datacollector.remove_neutral_tweets == "y" or datacollector.remove_neutral_tweets == "n":
            pass
        else:
            datacollector.remove_neutral_tweets = "w"
            raise ValueError
    except ValueError:
        print("One of the inputs is not correct, try again")

datacollector.start_collecting()
