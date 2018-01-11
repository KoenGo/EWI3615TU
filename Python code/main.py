from headline_processor import HeadlineProcessor
top_news = HeadlineProcessor()
print(top_news)
headlines = top_news.search_terms

from tweets_retriever import tweets
data_list = []
search_text = str(headlines[0][0]) + " " + str(headlines[0][1])
print("the search term is: " + str(search_text))
# search_text = input("For what search term do you want the sentiment? ")
number_of_tweets = input("How many tweets do you want to use? ")

from US_cities import us_cities
cities_dict = us_cities().load_cities()

data_list = tweets().get(search_text, number_of_tweets, data_list, cities_dict)

from sentiment_analyzer import sentiment
(polarity, data_list) = sentiment().get(data_list)
print("polarity =", polarity)

from location_map import map
map(data_list, cities_dict).print_map()
