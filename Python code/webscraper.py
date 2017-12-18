# Retrieve nouns from titles of news reports at http://edition.cnn.com/specials/last-50-stories
# use the nouns to find tweets and apply sentiment analysis
# remove retweets, tweets with similar contents

# which webscraper api to use?
# https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/

import requests
import re
from textblob import TextBlob
import datetime
from collections import Counter as counter
import operator


class Newspage():
    def __init__(self):
        self.url = "http://edition.cnn.com/specials/last-50-stories"
        self.source = requests.get(self.url).text
        self.timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.filename = 'newspage.txt'

        # Write whole source code to txt file
        with open(self.filename, 'w') as file:
            file.write(self.source)
            file.close()

    def __str__(self):
        top_five = [i for i in self.most_common_nouns(5)]
        return "News page created at: " + str(self.timestamp) + "\nWith top five: " + str(top_five)

    # FIXME

    def find_more(self):
        with open(self.filename, "a") as file:
            file.write(self.source)
        unique_headlines = set(self.get_headlines(self.filename))
        if self.get_headlines(self.filename) == unique_headlines:
            return "No new head lines found"
        else:
            return unique_headlines

    # Get headlines from the source code

    def get_headlines(self, filename):
        newspage = open(filename, 'rt').read()
        headlines = re.findall('(?<=<span class="cd__headline-text">)([^<]*)', newspage)
        return headlines

    # Method for extracting nouns
    # extract_nouns(sentence: str) -> [str]

    def extract_nouns(self, sentence):
        if isinstance(sentence, str):
            tb_sentence = TextBlob(sentence)
        else:
            raise Exception("Input must be string")
        result = []
        nounlist = tb_sentence.noun_phrases
        for i in nounlist:
            result += i.split(" ")
        return result

    # Extract all returns a list of lists containing all nouns
    # with each sublist corresponding to one headline

    def extract_all(self):
        result = []
        for headline in self.get_headlines(self.filename):
            result.append(self.extract_nouns(headline))
        return result

    def most_common_nouns(self, amount=10):
        """ Set amount to 0 for all nouns """
        all_nouns = []
        for noun_list in self.extract_all():
            all_nouns += noun_list

        noun_dict = counter(all_nouns)
        sorted_nouns = sorted(noun_dict.items(), key=operator.itemgetter(1), reverse=True)
        if int(amount) > 0:
            return sorted_nouns[:amount]
        else:
            return sorted_nouns


newspage = Newspage()
print(newspage.find_more())
