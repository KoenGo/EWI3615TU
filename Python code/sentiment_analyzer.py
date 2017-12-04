class sentiment:
    def get(self,list_of_tweets):
        from textblob import TextBlob
        positive = 0
        neutral = 0
        negative = 0

        for tweet in list_of_tweets:
            analysis = TextBlob(tweet)
            if analysis.sentiment.polarity > 0:
                positive += 1
            elif analysis.sentiment.polarity == 0:
                neutral += 1
            else:
                negative += 1
        mean_positive = positive/len(list_of_tweets)
        mean_neutral = neutral/len(list_of_tweets)
        mean_negative = negative/len(list_of_tweets)
        return (mean_positive, mean_neutral, mean_negative)
