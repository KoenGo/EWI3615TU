from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read text
d = path.dirname(__file__)
with open(path.join(d, 'datacollector_output/all_nouns.txt')) as file:
    rem = file.readlines()
    del rem[0::8]
    del rem[0::7]
    text = ' '.join(rem).replace('Story', ' ').replace("'", '')

# Generate a word cloud image
wordcloud = WordCloud(height=600, width=900, max_words=25, max_font_size=140).generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
