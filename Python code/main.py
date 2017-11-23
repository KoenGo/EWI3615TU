from tweets_retriever import tweets
search_text = input("What do you want to search for?")
number_of_tweets = input("How many tweets?")
list_of_tweets = tweets().get(search_text, number_of_tweets)

from sentiment_analyzer import sentiment
positivity = sentiment().get(list_of_tweets)
mean_positivity = sum(positivity)/len(positivity)
print(mean_positivity)
