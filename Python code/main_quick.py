from data_collector import DataCollector
datacollector = DataCollector()

datacollector.interval = 30
datacollector.number_of_intervals = 16
datacollector.neutral_tweets = 'y'
datacollector.start_collecting()