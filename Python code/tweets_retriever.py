class tweets:
    def get(self, search_text, number_of_tweets):
        import tweepy
        from tweepy import OAuthHandler

        import base64
        import requests
        import sys
        import re

        client_key = 'U0zHy6gQlsMpQumbEgHWXb7nm'
        client_secret = 'CbsDAod2sb31pLqVzBctFdoNMsTQPUZTm1ZInaXm62gmDP7J7I'
        access_token = ''
        access_secret = ''
        auth = OAuthHandler(client_key, client_secret)
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth)


        tweet_data = api.search(q=search_text, count=number_of_tweets,geocode="39.8,-95.583068847656,2500km")
        list_of_tweets = []
        list_of_coordinates = []
        count = 0
        for x in tweet_data:
            count += 1
            try:
                tweet = x.full_text
                tweet.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
                list_of_tweets.append(tweet)
            except AttributeError:
                tweet = x.text
                tweet.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
                list_of_tweets.append(tweet)
                print(x)
        print(list_of_tweets)
        print(count)
        return list_of_tweets

