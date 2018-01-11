from bs4 import BeautifulSoup as bs
import requests
import re

url = "https://news.google.com/news/headlines"
req = requests.get(url)
source = req.text

soup = bs(source,'html.parser')

with open('unformatted_source.txt', 'wb') as file:
    file.write(source.encode('utf-8', 'ignore'))

with open('full_source.txt', 'wb') as file:
     file.write(soup.prettify().encode('utf-8','ignore'))

#
# read lines, write lines to txt file until regex is found
#
def top_stories_to_file():
    with open('full_source.txt', 'r', errors='ignore') as file:
        lines = file.readlines()
        line_iter = iter(lines)
        line = next(line_iter)
        with open('top_stories_source.txt', 'w') as chopped_file:
            while True:
                if re.search('(\<a class="\w{6}" href="headlines/section/topic/WORLD\?ned=us" jslog="\d{5}; track: click;"\>)[^World]',line):
                    break
                chopped_file.write(line)
                line = next(line_iter)


def split_top_stories():
    with open('top_stories_source.txt', 'r', errors='ignore') as file:
        lines = file.readlines()
        line_iter = iter(lines)
        line = next(line_iter)
        split_nr = 1
        while True:
            grouped_headlines_file = 'headlines_{}.txt'.format(split_nr)
            with open(grouped_headlines_file, 'w') as gh_file:
                while True:
                    if re.search('View full coverage',line):
                        line = next(line_iter)
                        break
                    gh_file.write(line)
                    try:
                        line = next(line_iter)
                    except StopIteration:
                        return
            split_nr += 1
            if split_nr > 10:
                break

def get_headlines(file):
    """Automatically gets all head lines form a source file"""
    newspage = open(file, 'r').read()
    headlines = re.findall('jsname="\w{6}" role="heading" target="_blank">([^<]+)', newspage)
    return headlines

def headlines_to_file(headlines):
        with open('most_read_headlines.txt', 'w') as file:
            for headline in headlines:
                file.write(headline + "\n")

top_stories_to_file()
split_top_stories()