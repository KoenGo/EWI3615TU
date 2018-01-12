import json
import time
from tweepy.streaming import StreamListener
class listener(StreamListener):
    def __init__(self, time_limit_min, data_list, cities_dict):
        self.time_limit = float(time_limit_min) * 60
        self.data_list = data_list
        self.cities_dict = cities_dict
        self.progress_list = [self.time_limit*(x)/10 for x in range(1, 11)]
        self.start_time = time.time()
        self.current_time = 0

    def on_data(self, data):
        while self.current_time <= self.time_limit:
            json_data = json.loads(data)

            # check if Streamlistener returns a limit message instead of a tweet
            if "limit" in json_data:
                return True

            # determining whether a tweet has coordinates, place and users place of tweet
            # if a attribute exists it will be saved with the tweet in data_list
            coords = json_data["coordinates"]
            place = json_data["place"]
            user_place = json_data["user"]["location"]
            if coords is not None:
                self.data_list.append(json_data)
                if self.current_time > self.progress_list[0]:
                    print(str(int(self.progress_list[0]/self.time_limit*100)) + "% of time elapsed")
                    del self.progress_list[0]
                return True
            elif place is not None:
                if json_data["user"]["lang"] == "en":
                    self.data_list.append(json_data)
                if self.current_time > self.progress_list[0]:
                    print(str(int(self.progress_list[0]/self.time_limit*100)) + "% of time elapsed")
                    del self.progress_list[0]
                    return True
            elif json_data["user"]["location"] is not None:
                if user_place in self.cities_dict.keys():
                    json_data["coordinates"] = {}
                    json_data["coordinates"]["coordinates"] = self.cities_dict[user_place]
                    self.data_list.append(json_data)
                if self.current_time > self.progress_list[0]:
                    print(str(int(self.progress_list[0]/self.time_limit*100)) + "% of time elapsed")
                    del self.progress_list[0]
            self.current_time = time.time() - self.start_time
            return True
        else:
            return False
    def on_error(self, status):
        print(status)
