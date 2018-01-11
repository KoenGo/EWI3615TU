import json
from tweepy.streaming import StreamListener
class listener(StreamListener):
    def __init__(self, number_of_tweets, data_list, cities_dict):
        self.number_of_tweets = int(number_of_tweets)
        self.data_list = data_list
        self.cities_dict = cities_dict
        self.progress_list = [round(self.number_of_tweets*(x+1)/10) for x in range(10)]
        self.count = 0

    def on_data(self, data):
        if self.count <= self.number_of_tweets-1:
            json_data = json.loads(data)
            if "limit" in json_data:
                return True
            coords = json_data["coordinates"]
            place = json_data["place"]
            user_place = json_data["user"]["location"]
            if coords is not None:
                self.data_list.append(json_data)
                if (self.count+1) in self.progress_list:
                    print(str(int(round((self.count+1)/self.number_of_tweets*10)*10)) + "% of tweets retrieved")
                self.count += 1
                return True
            elif place is not None:
                if json_data["user"]["lang"] == "en":
                    self.data_list.append(json_data)
                    if (self.count+1) in self.progress_list:
                        print(str(int(round((self.count+1)/self.number_of_tweets*10)*10)) + "% of tweets retrieved")
                    self.count += 1
                    return True
            elif json_data["user"]["location"] is not None:
                if user_place in self.cities_dict.keys():
                    json_data["coordinates"] = {}
                    json_data["coordinates"]["coordinates"] = self.cities_dict[user_place]
                    self.data_list.append(json_data)
                    if (self.count+1) in self.progress_list:
                        print(str(int(round((self.count+1)/self.number_of_tweets*10)*10)) + "% of tweets retrieved")
                    self.count += 1
            return True
        else:
            return False
    def on_error(self, status):
        print(status)
