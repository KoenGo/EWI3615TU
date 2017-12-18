import json
from tweepy import Stream
from tweepy import OAuthHandler
from stream_listener import listener
from tweepy.streaming import StreamListener
class tweets():
    def get(self, search_text, number_of_tweets):
            # import base64
            # import requests
            # import sys
            # import re

        client_key = 'U0zHy6gQlsMpQumbEgHWXb7nm'
        client_secret = 'CbsDAod2sb31pLqVzBctFdoNMsTQPUZTm1ZInaXm62gmDP7J7I'
        access_token = '932924142906761216-25dcDBqKSnXX2sDJKmF7MYGbuQ2EgXQ'
        access_secret = 'ZcRkzfxTG05pHlQhmEywM45z7Vh8u1ymCopKU5OMRBRCw'


        auth = OAuthHandler(client_key, client_secret)
        auth.set_access_token(access_token, access_secret)

        twitterStream = Stream(auth, listener())
        twitterStream.filter(locations=[-152.1507174141,5.7544951484,-41.8114775055,67.2290194409])
        return data_list


        #tweet_data = api.search(q=search_text, count=number_of_tweets, tweet_mode='extended', geocode="39.8,-95.583068847656,2500km")
        #list_of_tweets = []
        #list_of_coordinates = []
        #count = 0
        #for x in tweet_data:
        #    count += 1
        #    try:
        #        tweet = x.full_text
        #        tweet.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
        #        list_of_tweets.append(tweet)
        #        print(x.coordinates)
        #    except AttributeError:
        #        pass
        #print(list_of_tweets)
        #print(count)
        #return list_of_tweets

