from textblob import TextBlob


class sentiment:
    def get(self, data_list, neutral_tweets):
        total_polarity = 0
        count = 0
        remove_list = []
        list_of_colors = ['#8B0000', '#FF0000', '#FF8C00', '#FFA500', '#FFFF00', '#ADFF2F', '#9ACD32', '#008000',
                          '#006400']
        for tweet in data_list:
            try:
                analysis = TextBlob(tweet['full_text'])
            except KeyError:
                analysis = TextBlob(tweet['text'])

            # Save polarity of individual tweet
            polarity = analysis.sentiment.polarity
            data_list[count]["polarity"] = polarity

            # Total polarity of all tweets
            total_polarity += polarity

            # Pick marker color
            number = round((polarity + 1) * 4)
            if neutral_tweets == "y":
                if number == 4:
                    remove_list.append(tweet)
            data_list[count]["color"] = list_of_colors[number]


            count += 1

        for tweet in remove_list:
            data_list.remove(tweet)
        return total_polarity, data_list
