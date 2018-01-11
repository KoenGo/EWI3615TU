class sentiment:
    def get(self,data_list):
        from textblob import TextBlob
        polarity = 0

        for tweet in data_list:
            try:
                analysis = TextBlob(tweet['full_text'])
            except KeyError:
                analysis = TextBlob(tweet['text'])
            polarity += analysis.sentiment.polarity
        return (polarity)
