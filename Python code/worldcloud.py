from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image


def generate_wordcloud_image():
    # Read text and remove unwanted text
    d = path.dirname(__file__)
    with open(path.join(d, 'datacollector_output/all_nouns.txt')) as file:
        rem = file.readlines()
        del rem[0::8]
        del rem[0::7]
        text = ' '.join(rem).replace("'", '')

    # Load wordcloud mask image
    trump_img_wc = np.array(Image.open(path.join(d, 'trump_er_new.png')))
    stopwords = set(STOPWORDS)
    stopwords.add("Story")

    # Generate a word cloud image
    wc = WordCloud(max_words=2000, min_font_size=6, max_font_size=70, stopwords=stopwords, background_color="white",
                   mask=trump_img_wc, relative_scaling=0.65)
    wc.generate(text)
    image_colors = ImageColorGenerator(trump_img_wc)

    # Draw and save wordcloud
    plt.figure(figsize=(1150 / 600, 793 / 600))
    plt.imshow(wc.recolor(color_func=image_colors), interpolation='bilinear')
    plt.axis("off")
    plt.savefig('trump_wordcloud.png', dpi=600)

    # Merge images
    foreground = Image.open('trump_head.png')
    background = Image.open('trump_wordcloud.png')
    Image.alpha_composite(background, foreground).save("trump_layered.png")

generate_wordcloud_image()