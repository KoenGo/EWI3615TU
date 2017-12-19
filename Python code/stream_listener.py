import json
import sys
from tweepy.streaming import StreamListener
count = 0
class listener(StreamListener):
    def __init__(self, number_of_tweets, data_list):
        self.number_of_tweets = number_of_tweets
        self.data_list = data_list

    def on_data(self, data):
        global count
        #How many tweets you want to find, could change to time based
        try:
            if count <= int(self.number_of_tweets)-1:
                json_data = json.loads(data)
                coords = json_data["coordinates"]
                if coords is not None:
                    print(coords["coordinates"])
                    #lon = coords["coordinates"][0]
                    #lat = coords["coordinates"][1]

                    self.data_list.append(json_data)

                    count += 1
                return True
            else:
                return False
        except:
            return True

    def on_error(self, status):
        print(status)
