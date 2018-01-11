from tweets_retriever import tweets
data_list = []
search_text = ""
text_or_location = ""
text_or_location = input("Do you want to search location of text? type l for location and t for text:")
while text_or_location != "l" and text_or_location != "t":
    text_or_location = input("Your input is not correct, type l for location and t for text:")
if text_or_location == "t":
    search_text = input("For what search term do you want the sentiment? ")
number_of_tweets = input("How many tweets do you want to use? ")

from US_cities import us_cities
cities_dict = us_cities().load_cities()

data_list = tweets().get(search_text, text_or_location, number_of_tweets, data_list, cities_dict)

from sentiment_analyzer import sentiment
polarity = sentiment().get(data_list)
print("polarity =", polarity)

map(data_list, text_or_location, cities_dict).print_map()
