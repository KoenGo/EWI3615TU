from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image

# Read text
d = path.dirname(__file__)
with open(path.join(d, 'datacollector_output/all_nouns.txt')) as file:
    rem = file.readlines()
    del rem[0::8]
    del rem[0::7]
    text = ' '.join(rem).replace("'", '')

trump_img_wc = np.array(Image.open(path.join(d, 'trump_er_new.png')))
trump_img = np.array(Image.open('trump.png'))
stopwords = set(STOPWORDS)
stopwords.add("Story")

# Generate a word cloud image
wc = WordCloud(max_words=2000, min_font_size=6, max_font_size=70, stopwords=stopwords, background_color="white",
               mask=trump_img_wc, relative_scaling=0.65)
wc.generate(text)

image_colors = ImageColorGenerator(trump_img_wc)  # default_color=(255,255,255))

# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.show()
# plt.imshow(wc.recolor(color_func=image_colors), interpolation="spline-16")
# plt.axis("off")
# plt.show()
plt.figure(figsize=(5/3000*1150,5/3000*793))
plt.imshow(wc.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis("off")
plt.savefig('trump_wordcloud.png', dpi=600)
foreground = Image.open('trump_head.png')
background = Image.open('trump_wordcloud.png')
Image.alpha_composite(background, foreground).save("trump_layered.png")
