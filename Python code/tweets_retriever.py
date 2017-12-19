import json
from tweepy import Stream
from tweepy import OAuthHandler
from stream_listener import listener
class tweets():
    def get(self, search_text,number_of_tweets, data_list):
        client_key = 'U0zHy6gQlsMpQumbEgHWXb7nm'
        client_secret = 'CbsDAod2sb31pLqVzBctFdoNMsTQPUZTm1ZInaXm62gmDP7J7I'
        access_token = '932924142906761216-25dcDBqKSnXX2sDJKmF7MYGbuQ2EgXQ'
        access_secret = 'ZcRkzfxTG05pHlQhmEywM45z7Vh8u1ymCopKU5OMRBRCw'


        auth = OAuthHandler(client_key, client_secret)
        auth.set_access_token(access_token, access_secret)

        twitterStream = Stream(auth, listener(number_of_tweets, data_list))
        twitterStream.filter(locations=[-129.0506786523,24.7249990876,-69.1287372546,50.2424298384])
        return data_list
