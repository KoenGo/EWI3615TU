# Retrieve nouns from titles of news reports at http://edition.cnn.com/specials/last-50-stories
# use the nouns to find tweets and apply sentiment analysis
# remove retweets, tweets with similiar contents

# which webscraper api to use?
# https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/

import requests
import re
import codecs
from textblob import TextBlob
import bs4 as beautifulsoup

url  = "http://edition.cnn.com/specials/last-50-stories"
newspage = requests.get(url)
splitlines = re.findall("(.{100})",newspage.text)



# Write content to txt file
f = codecs.open('newspage.txt', encoding='utf-8', mode='w')
for line in splitlines:
    f.write(line + "\n")
f.close()

# Extract nouns
blob = TextBlob("Atlanta airport outage complicates insanely busy holiday travel")
print(blob.noun_phrases)