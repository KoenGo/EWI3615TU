import json
from tweepy.streaming import StreamListener
count = 0
data_list = []
class listener(StreamListener):
    def on_data(self, data):
        global count
        global data_list
        #How many tweets you want to find, could change to time based
        try:
            if count <= 10:
                json_data = json.loads(data)
                coords = json_data["coordinates"]
                if coords is not None:
                    print(coords["coordinates"])
                    #lon = coords["coordinates"][0]
                    #lat = coords["coordinates"][1]

                    data_list.append(json_data)

                    count += 1
                    print(count)
                return True
            else:
                exit("Enough tweets")
        except:
            return True

    def on_error(self, status):
        print(status)
