from headline_processor import HeadlineProcessor
from tweets_retriever import tweets
from US_cities import us_cities
from sentiment_analyzer import sentiment
from location_map import map

# Scrape google news site, collect headlines and extract most occurring nouns.
top_news = HeadlineProcessor()
print(top_news)
headlines = top_news.search_terms

# Plug in the first 2 most occurring nouns from the first story
story = 0 # Which story to pick? 0-5, 0 is the top story
search_text = str(headlines[story][0]) + " " + str(headlines[story][1])
print("The search term is: " + str(search_text))
time_limit_h = input("How long do you want to search (hours): ")

# Load cities dictionary
cities_dict = us_cities().load_cities()

# Get a list of tweets
data_list = tweets().get(search_text, time_limit_h, cities_dict)

# Perform sentiment analysis on all tweets
(polarity, data_list) = sentiment().get(data_list)
print("polarity =", polarity)

# Draw map
map(data_list, cities_dict, timestamp = '').print_map()


