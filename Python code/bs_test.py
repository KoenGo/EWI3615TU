from bs4 import BeautifulSoup as bs
import requests
import re

url = "https://news.google.com/news/headlines"
req = requests.get(url)
source = req.text

soup = bs(source,'html.parser')

with open('bs_source.txt', 'wb') as file:
     file.write(soup.prettify().encode('utf-8','ignore'))


with open('bs_strings.txt', 'wb') as file:
    for string in soup.strings:
        file.write(string.encode('utf-8','ignore'))


#
# read lines, write lines to txt file until regex is found
#

with open('bs_source.txt', 'r', errors='ignore') as file:
    lines = file.readlines()
    line_iter = iter(lines)
    line = lines[0]
    with open('chopped_source.txt', 'w') as chopped_file:
        while True:
            if re.search('(\<a class="\w{6}" href="headlines/section/topic/WORLD\?ned=us" jslog="\d{5}; track: click;"\>)[^World]',line):
                break
            chopped_file.write(line)
            line = next(line_iter)

def get_headlines():
    newspage = open('chopped_source.txt', 'r').read()
    headlines = re.findall('jsname="\w{6}" role="heading" target="_blank">([^<]+)', newspage)
    return headlines

def headlines_to_file(headlines):
        with open('most_read_headlines.txt', 'w') as file:
            for headline in headlines:
                file.write(headline + "\n")

print(get_headlines())
headlines_to_file(get_headlines())