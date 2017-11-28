class sentiment:
    def get(self,string_of_tweets):
        positive = []
        neutral = []
        negative = []
        import requests
        data = [
        ('text', string_of_tweets),
        ]
        response = requests.post('http://text-processing.com/api/sentiment/', data=data)
        data = response.json()
        mean_positive = data["probability"]["pos"]
        mean_neutral = data["probability"]["neutral"]
        mean_negative = data["probability"]["neg"]
        return (mean_positive, mean_neutral, mean_negative)
