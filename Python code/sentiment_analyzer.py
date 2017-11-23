class sentiment:
    def get(self,list_of_tweets):
        positivity = []
        import requests
        for tweet in list_of_tweets:
            data = [
            ('text', tweet),
            ]
            response = requests.post('http://text-processing.com/api/sentiment/', data=data)
            data = response.json()
            positivity.append(data["probability"]["pos"])
        return positivity
