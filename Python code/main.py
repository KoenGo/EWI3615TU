from tweets_retriever import tweets
data_list = []
search_text = input("For what search term do you want the sentiment? ")
number_of_tweets = input("How many tweets do you want to use? ")
data_list = tweets().get(search_text, number_of_tweets, data_list)


# from sentiment_analyzer import sentiment
# (mean_positive, mean_neutral, mean_negative) = sentiment().get(list_of_tweets)
# print("positive =", mean_positive)
# print("neutral =", mean_neutral)
# print("negative =",mean_negative)
