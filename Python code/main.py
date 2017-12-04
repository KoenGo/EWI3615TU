from tweets_retriever import tweets
search_text = input("For what search term do you want the sentiment?")
number_of_tweets = input("How many tweets do you want to use?")
list_of_tweets = tweets().get(search_text, number_of_tweets)

from sentiment_analyzer import sentiment
(mean_positive, mean_neutral, mean_negative) = sentiment().get(list_of_tweets)
print("positive = " + str(mean_positive))
print("neutral = " + str(mean_neutral))
print("negative = " + str(mean_negative))
