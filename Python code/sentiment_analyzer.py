class sentiment:
    def get(self, data_list):
        from textblob import TextBlob
        total_polarity = 0
        count = 0
        list_of_colors = ['#8B0000', '#FF0000', '#FF8C00', '#FFA500', '#FFFF00', '#ADFF2F', '#9ACD32', '#008000', '#006400']
        for tweet in data_list:
            try:
                analysis = TextBlob(tweet['full_text'])
            except KeyError:
                analysis = TextBlob(tweet['text'])
            polarity = analysis.sentiment.polarity
            total_polarity += polarity
            number = round((polarity+1)*4)
            data_list[count]["color"] = list_of_colors[number]
            count += 1
        return (total_polarity, data_list)
