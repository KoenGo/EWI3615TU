from tweets_retriever import tweets
search_text = input("What do you want to search for?")
number_of_tweets = input("How many tweets?")
list_of_tweets = tweets().get(search_text, number_of_tweets)
for tweet in list_of_tweets:
    print(tweet)
