from bs4 import BeautifulSoup as bs
import requests
import re

url = "https://news.google.com/news/headlines"
req = requests.get(url)
source = req.text

soup = bs(source,'html.parser')

with open('raw_source.txt', 'wb') as file:
    file.write(source.encode('utf-8', 'ignore'))

with open('bs_source.txt', 'wb') as file:
     file.write(soup.prettify().encode('utf-8','ignore'))


with open('bs_strings.txt', 'wb') as file:
    for string in soup.strings:
        file.write(string.encode('utf-8','ignore'))


#
# read lines, write lines to txt file until regex is found
#
def top_stories_to_file():
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

# def split_top_stories():
#     with open('chopped_source.txt', 'r', errors='ignore') as file:
#         while

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

# <c-wiz jsrenderer="WluEBc" class="ROONz H7eG6b" jsshadow jsdata="deferred-i1" data-p="%.@.&quot;headlines&quot;,null,null,null,&quot;us&quot;]
# " jscontroller="GILUZe" jsaction="click:cOuCgd;RI2Xre:Vtdxob;" data-node-index="0;0" jsmodel="hc6Ubd">
# get turned into
# <c-wiz class="ROONz H7eG6b" data-node-index="0;0" data-p='%.@."headlines",null,null,null,"us"]
# ' jsaction="click:cOuCgd;RI2Xre:Vtdxob;" jscontroller="GILUZe" jsdata="deferred-i1" jsmodel="hc6Ubd" jsrenderer="WluEBc" jsshadow="">