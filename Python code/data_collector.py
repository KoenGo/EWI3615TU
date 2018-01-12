import os
from headline_processor import HeadlineProcessor
from tweets_retriever import tweets
from US_cities import us_cities
from sentiment_analyzer import sentiment
from location_map import map


class DataCollector:
    def __init__(self):
        self.make_dir()
        self.interval = 10  # Minutes
        self.timestamp = None
        self.story = 0
        self.cities_dict = us_cities().load_cities()

    def make_dir(self):
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, 'datacollector_output')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

    def info_to_file(self, tweet_list):
        with open('datacollector_output/tweet_polarity.txt', 'a') as polarity_file:
            polarity_file.write(self.timestamp)
            for tweet in tweet_list:
                polarity_file.write(str(tweet['polarity']) + "\n")

    def gather_tweets(self, interval, story=0):
        top_news = HeadlineProcessor()
        headlines = top_news.search_terms
        self.timestamp = top_news.timestamp
        search_text = str(headlines[story][0]) + " " + str(headlines[story][1])

        with open('datacollector_output/headlines.txt', 'a') as headline_file:
            headline_file.write("Headlines at " + self.timestamp + "\n")
            headline_file.write(str(top_news.headlines) + "\n")
        with open('datacollector_output/search_terms.txt', 'a') as term_file:
            term_file.write("Searchterms at " + self.timestamp + "\n")
            term_file.write(str(headlines) + "\n")

        return tweets().get(search_text, interval, self.cities_dict)

    def get_sentiment(self, input_tweet_list):
        (polarity, output_tweet_list) = sentiment().get(input_tweet_list)
        return output_tweet_list

    def draw_map(self, data_list, cities_dict, timestamp):
        return map(data_list, cities_dict, timestamp).print_map()

    def start_collecting(self):
        """"Starts collecting until stopped, returning information at interval time"""
        while True:
            print("Gather tweets")
            tweets_raw = self.gather_tweets(self.interval, self.story)
            print("Get sentiment")
            tweets_sentiment = self.get_sentiment(tweets_raw)
            self.info_to_file(tweets_raw)
            print("Draw map")
            map_timestamp = self.timestamp.replace(":", "-")
            self.draw_map(tweets_sentiment, self.cities_dict, map_timestamp)


datacollector = DataCollector()
datacollector.interval = 1
datacollector.start_collecting()
