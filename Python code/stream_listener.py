import json
import sys
from tweepy.streaming import StreamListener
count = 0
class listener(StreamListener):
    def __init__(self, number_of_tweets, data_list, text_or_location):
        self.number_of_tweets = number_of_tweets
        self.data_list = data_list
        self.text_or_location = text_or_location

    def on_data(self, data):
        global count

        if self.text_or_location == "l":
            try:
                if count <= int(self.number_of_tweets)-1:
                    json_data = json.loads(data)
                    coords = json_data["coordinates"]
                    if coords is not None:
                        print(coords["coordinates"])

                        self.data_list.append(json_data)

                        count += 1
                    return True
                else:
                    return False
            except:
                return True
        else:
            if count <= int(self.number_of_tweets)-1:
                json_data = json.loads(data)
                self.data_list.append(json_data)
                count += 1
            else:
                return False
    def on_error(self, status):
        print(status)
