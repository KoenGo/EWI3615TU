from headline_processor import HeadlineProcessor
top_news = HeadlineProcessor()
print(top_news)
headlines = top_news.search_terms

from tweets_retriever import tweets
data_list = []
search_text = str(headlines[0][0]) + " " + str(headlines[0][1])
print("the search term is: " + str(search_text))
time_limit_h = input("How long do you want to search (hours): ")

from US_cities import us_cities
cities_dict = us_cities().load_cities()

data_list = tweets().get(search_text, time_limit_h, data_list, cities_dict)

from sentiment_analyzer import sentiment
(polarity, data_list) = sentiment().get(data_list)
print("polarity =", polarity)

from location_map import map
map(data_list, cities_dict).print_map()
