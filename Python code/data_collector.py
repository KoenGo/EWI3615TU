import os
import time
from headline_processor import HeadlineProcessor
from tweets_retriever import tweets
from US_cities import us_cities
from sentiment_analyzer import sentiment
from location_map import map


class DataCollector:
    """"Starts collecting until stopped, returning information at interval time"""
    def __init__(self):
        self.make_dir()
        self.interval = 0  # Minutes
        self.number_of_intervals = 0
        self.timestamp = None
        self.story = 0
        self.cities_dict = us_cities().load_cities()
        self.remove_neutral_tweets = 'n' # 'y' for yes
        self.search_text = None
        self.write_whole_tweet = 'disabled'

    def make_dir(self):
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, 'datacollector_output')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

    def info_to_file(self, tweet_list):
        if self.write_whole_tweet.lower() == 'enabled':
            with open('datacollector_output/whole_tweet.txt', 'a', encoding='utf-8', errors='ignore') as whole_tweet_file:
                whole_tweet_file.write("Tweets with polarities at: {0}\n".format(self.timestamp))
                for tweet in tweet_list:
                    try:
                        whole_tweet_file.write("Tweet: {0} Polarity: {1}\n".format(tweet['full_text'], tweet['polarity']))
                    except KeyError:
                        whole_tweet_file.write("Tweet: {0} Polarity: {1}\n".format(tweet['text'], tweet['polarity']))
        elif self.write_whole_tweet.lower() == 'disabled':
            with open('datacollector_output/tweet_polarity.txt', 'a') as polarity_file:
                polarity_file.write(
                    "Polarities at: {0} for search terms: \"{1}\"\n".format(self.timestamp, self.search_text))
                for tweet in tweet_list:
                    polarity_file.write(str(tweet['polarity']) + "\n")
        else:
            raise Exception("Invalid parameter provided!")



    def gather_tweets(self, interval, story=0):
        top_news = HeadlineProcessor()
        self.headline_nouns = top_news.search_terms
        self.timestamp = top_news.timestamp
        self.search_text = str(self.headline_nouns[story][0]) + " " + str(self.headline_nouns[story][1])
        print("Current search:\"{0}\"".format(self.search_text))
        with open('datacollector_output/headlines.txt', 'a') as headline_file:
            headline_file.write("Headlines at " + self.timestamp + "\n")
            headline_file.write(str(top_news.headlines) + "\n")
        with open('datacollector_output/search_terms.txt', 'a') as term_file:
            term_file.write("Search terms at " + self.timestamp + "\n")
            term_file.write(str(self.headline_nouns) + "\n")

        return tweets().get(self.search_text, interval, self.cities_dict)

    def get_sentiment(self, input_tweet_list, neutral_tweets):
        (polarity, output_tweet_list) = sentiment().get(input_tweet_list, neutral_tweets)
        return output_tweet_list

    def draw_map(self, data_list, cities_dict, timestamp):
        return map(data_list, cities_dict, timestamp).print_map()

    def start_collecting(self):
        interval = 0
        while interval < self.number_of_intervals:

            # Pulling headlines, extracting tweets
            print("Gathering tweets...({0}/{1})".format(interval+1, self.number_of_intervals))
            tweets_raw = self.gather_tweets(self.interval, self.story)

            # Calculating sentiment on tweets
            print("Calculating sentiment...({0}/{1})".format(interval+1, self.number_of_intervals))
            tweets_sentiment = self.get_sentiment(tweets_raw, self.remove_neutral_tweets)
            self.info_to_file(tweets_sentiment)

            # Generate map
            print("Generating map...({0}/{1})".format(interval+1, self.number_of_intervals))
            map_filename_extension = "{0}_".format(self.search_text.replace(" ","_")) + str(self.timestamp.replace(":", "-"))
            self.draw_map(tweets_sentiment, self.cities_dict, map_filename_extension)
            print("Interval ({0}/{1}) completed \n".format(interval+1, self.number_of_intervals))
            interval += 1
        print("Done!")

    def start_collecting_nouns(self):
        interval = 0
        runtime = self.interval
        while interval < self.number_of_intervals:
            print("Gathering nouns...({0}/{1})".format(interval + 1, self.number_of_intervals))
            start_time = time.time()
            headline_processor = HeadlineProcessor()
            timestamp = headline_processor.timestamp
            with open('datacollector_output/all_nouns.txt', 'a') as noun_file:
                noun_file.write("Nouns and headlines retrieved at: " + timestamp + "\n")
                noun_file.write("Headlines: {0}\n".format(headline_processor.headlines))
                for count, nouns in enumerate(headline_processor):
                    noun_file.write("Story {0}: {1}\n".format(count + 1, nouns))

            # Time the loop should rest after retrieving headlines. Runtime is in minutes
            sleep_time = 60*runtime-(time.time()-start_time)
            if sleep_time > 0:
                time.sleep(sleep_time)
            else:
                raise Exception("Interval time is too short!")
            interval += 1