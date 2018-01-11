import json
from tweepy import Stream
from tweepy import OAuthHandler
from stream_listener import listener
class tweets():
    def get(self, search_text, text_or_location, number_of_tweets, data_list, cities_dict):
        client_key = 'U0zHy6gQlsMpQumbEgHWXb7nm'
        client_secret = 'CbsDAod2sb31pLqVzBctFdoNMsTQPUZTm1ZInaXm62gmDP7J7I'
        access_token = '932924142906761216-25dcDBqKSnXX2sDJKmF7MYGbuQ2EgXQ'
        access_secret = 'ZcRkzfxTG05pHlQhmEywM45z7Vh8u1ymCopKU5OMRBRCw'


        auth = OAuthHandler(client_key, client_secret)
        auth.set_access_token(access_token, access_secret)

        twitterStream = Stream(auth, listener(number_of_tweets, data_list, text_or_location, cities_dict))
        if text_or_location is "l":
            twitterStream.filter(locations=[-124.3150818348,24.3677378899,-68.5045349598,49.1534179227])
        else:
            twitterStream.filter(track=[search_text])
        return data_list
