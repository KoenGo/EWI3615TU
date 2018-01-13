from data_collector import DataCollector

# datacollector = DataCollector()
# datacollector.interval = 30
# datacollector.number_of_intervals = 16
# datacollector.neutral_tweets = 'y'
# datacollector.start_collecting()

nouncollector = DataCollector()
nouncollector.interval = 5
nouncollector.number_of_intervals = 10
nouncollector.start_collecting_nouns()
