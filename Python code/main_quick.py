from data_collector import DataCollector

datacollector = DataCollector()
datacollector.interval = 10
datacollector.number_of_intervals = 100
datacollector.remove_neutral_tweets = 'y'
datacollector.write_whole_tweet = 'enabled'
datacollector.story = 0
datacollector.start_collecting()

# nouncollector = DataCollector()
# nouncollector.interval = 0.5
# nouncollector.number_of_intervals = 1
# nouncollector.start_collecting_nouns()