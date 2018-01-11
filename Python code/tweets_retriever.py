from tweepy import Stream
from tweepy import OAuthHandler
from stream_listener import listener
class tweets():
    def get(self, search_text, number_of_tweets, data_list, cities_dict):

        # twitter developer keys
        client_key = 'U0zHy6gQlsMpQumbEgHWXb7nm'
        client_secret = 'CbsDAod2sb31pLqVzBctFdoNMsTQPUZTm1ZInaXm62gmDP7J7I'
        access_token = '932924142906761216-25dcDBqKSnXX2sDJKmF7MYGbuQ2EgXQ'
        access_secret = 'ZcRkzfxTG05pHlQhmEywM45z7Vh8u1ymCopKU5OMRBRCw'

        # authentication with developer keys
        auth = OAuthHandler(client_key, client_secret)
        auth.set_access_token(access_token, access_secret)

        # starting the Streamlistener with the given search text for number_of_tweets
        twitterStream = Stream(auth, listener(number_of_tweets, data_list, cities_dict))
        twitterStream.filter(track=[search_text])
        return data_list
