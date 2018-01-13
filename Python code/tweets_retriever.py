from tweepy import Stream
from tweepy import OAuthHandler
from stream_listener import listener
class tweets:
    def get(self, search_text, time_limit_h, cities_dict, data_list=list()):

        # twitter developer keys
        client_key = '6s9eBNhnhmE97lSpmUo77q1MR'
        client_secret = '6bkoUN5CMJOWvvUsCz84YOkZdmk4YA7n3gKdFlfaKQkvSwEQOb'
        access_token = '952207340060758016-fUwFBDSOsAwzpMNrk2VRmDikvOXYwfY'
        access_secret = 'RKKY83ZEXUW1kUB5NN3KfONmJBqFy2VYX0l7jBpIlAX6W'

        # authentication with developer keys
        auth = OAuthHandler(client_key, client_secret)
        auth.set_access_token(access_token, access_secret)

        # starting the Streamlistener with the given search text for number_of_tweets
        print("0% of time elapsed")
        twitterStream = Stream(auth, listener(time_limit_h, data_list, cities_dict))
        twitterStream.filter(track=[search_text])
        return data_list