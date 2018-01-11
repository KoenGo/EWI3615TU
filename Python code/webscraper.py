# Retrieve nouns from titles of news reports at http://edition.cnn.com/specials/last-50-stories
# use the nouns to find tweets and apply sentiment analysis
# remove retweets, tweets with similar contents

# which webscraper api to use?
# https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/

import requests
import re
from textblob import TextBlob
import datetime
import time
from collections import Counter
import operator
import bs4 as bs

class NewsPage():
    def __init__(self):
        self.url = "https://news.google.com/news/headlines"
        self.source = requests.get(self.url).text
        self.timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.filename = 'newspage.txt'
        self.headlines = None

        # Write whole source code to txt file
        try:
            with open(self.filename, 'w') as file:
                file.write(str(self.source))
                file.close()
        except IOError as err:
                print("{0}".format(err))

    def __str__(self):
        return "News page created at: " + str(self.timestamp)

    #  Pull more headlines from the website
    def find_more(self):
        self.old_headlines = self.current_headlines

        with open(self.filename, "w") as file:
            file.write(self.source)
        self.current_headlines = self.get_headlines()
        if set(self.current_headlines) == set(self.old_headlines):
            return "No new headlines found"
        else:
            return list(set(self.current_headlines).difference(self.old_headlines))

    # Get headlines from the source code (which is in the text file)

    def get_headlines(self):
        #newspage = open(self.filename, 'rt').read()
        self.headlines = re.findall('(?<= jsname="[\w]{6}" role="heading" aria-level="3" >)([^<]+)', self.source)
        return self.headlines

    def headlines_to_file(self):
        if self.headlines is not None:
            with open('headlines.txt', 'w') as file:
                for headline in self.headlines:
                    file.write(headline + "\n")
        else:
            self.headlines = self.get_headlines()
            with open('headlines.txt', 'w') as file:
                for headline in self.headlines:
                    file.write(headline + "\n")

    def retrieve_top_stories(self):

        pass



    # Method for extracting nouns
    # extract_nouns(sentence: str) -> [str]

    def extract_nouns(self, sentence):
        if isinstance(sentence, str):
            tb_sentence = TextBlob(sentence)
        else:
            raise Exception("Input must be string")
        noun_list = tb_sentence.noun_phrases
        return [i.split(" ") for i in noun_list]

    # Extract all returns a list of lists containing all nouns
    # with each sublist corresponding to one headline

    def extract_all(self):
        result = []
        for headline in self.get_headlines():
            result.append(self.extract_nouns(headline))
        return result

    def most_common_nouns(self, amount=10):
        """ Set amount to 0 for all nouns """
        all_nouns = []
        for noun_list in self.extract_all():
            all_nouns += noun_list
        # Remove CNN and 's from the list
        all_nouns = [item for sublist in all_nouns for item in sublist]
        noun_dict = Counter(all_nouns)
        sorted_nouns = sorted(noun_dict.items(), key=operator.itemgetter(1), reverse=True)
        if int(amount) > 0:
            return sorted_nouns[:amount]
        else:
            return sorted_nouns

a = NewsPage().get_headlines()

print(a)

# while True:
#     time.sleep(0.1)
#     inp = input("\nInput 'n' to pull more headlines, 's' to stop: ")
#     if inp.lower() == "s":
#         break
#     elif inp.lower() == "n":
#         print(newspage.find_more())
#     elif inp.lower() == "show":
#         print(newspage)
#     else:
#         continue
