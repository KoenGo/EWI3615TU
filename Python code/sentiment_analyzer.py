class sentiment:
    def get(self,list_of_tweets):
        positive = []
        neutral = []
        negative = []
        import requests
        for tweet in list_of_tweets:
            data = [
            ('text', tweet),
            ]
            response = requests.post('http://text-processing.com/api/sentiment/', data=data)
            data = response.json()
            positive.append(data["probability"]["pos"])
            neutral.append(data["probability"]["neutral"])
            negative.append(data["probability"]["neg"])
            mean_positive = sum(positive)/len(positive)
            mean_neutral = sum(neutral)/len(neutral)
            mean_negative = sum(negative)/len(negative)
        return (mean_positive, mean_neutral, mean_negative)
