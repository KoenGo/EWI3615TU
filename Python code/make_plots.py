import numpy as np
import matplotlib.pyplot as plt
import re

with open('datacollector_output/all_nouns.txt') as file:
    lines = file.readlines()
    total_stories = 0
    headline_count = []
    avg_nouns_matrix = []
    for line in lines:
        if re.search('(?=Headlines:).*', line):
            stories = re.findall('\[(.+?)\]', line)
            for story in stories:
                headline_count.append(len(re.split('[\'\"], [\'\"]', story)))
                total_stories += 1
        if re.search("\('\S+', (\d)\)", line):
            whole_match = list(map(int, re.findall("\('\S+', (\d)\)", line)))[:10]
            if len(whole_match) < 10:
                whole_match += [0]*(10-len(whole_match))
            avg_nouns_matrix.append(list(map(int, whole_match)))


    avg_hl_story = np.sum(headline_count)/total_stories
    x = np.matrix(avg_nouns_matrix)
    means = np.array(x.mean(0)).flatten()

    print("Total stories = {0} total_headlines = {1}".format(total_stories, np.sum(headline_count)))
    print("Avg headline/story = {0}".format(avg_hl_story))
    print("Mean occurence of the 1st-10th most common noun in each story: {0}".format(means))
    fraction1 = (means[0] + means[1])/np.sum(means)
    print("First and second noun account for {0}% of total nouns (on average)".format(fraction1*100))
    fraction2 = (means[0] + means[1] + means[2]) / np.sum(means)
    print("First three nouns account for {0}% of total nouns (on average)".format(fraction2*100))


# Sample size: 815 stories, 4147 headlines

x = np.arange(10)
plt.figure(figsize=(7,15))
plt.subplot(211)
plt.bar(x, means, zorder=2, color='blue')
plt.xticks(x, ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'])
plt.title('Average occurrences vs. noun rank')
plt.xlabel('Noun rank (most occurring)')
plt.ylabel('Average occurrences')
plt.grid(zorder=0)
for a,b in zip(x, means):
    plt.text(a-0.3, b+0.02, str(round(b,2)))

plt.subplot(212)
x = np.arange(10)
percentages = []
for mean in np.cumsum(means):
    percentages.append((mean/np.sum(means)*100))

for a,b in zip(x, percentages):
    plt.text(a-0.3, b+0.26, str(round(b,2)))

plt.bar(x, percentages, zorder=2, color='crimson')
plt.xticks(x, ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'])
plt.title('Average cummulative percentage vs. noun rank')
plt.xlabel('Noun rank (most occurring)')
plt.ylabel('Percentage')
plt.grid(zorder=0)
plt.savefig('graphs_nouns.eps', format='eps', dpi=800)
plt.show()

plt.figure(figsize=(7,3))
x = ['Coordinates','Coordinates and place','Coordinates, place and user place']
y = [2, 94, 7370]
plt.bar(x, y, zorder=2, color='blue')
for i in range(3):
    plt.text(i-0.2, y[i]+20, str(y[i]) + " tweets")
plt.title('Average cummulative percentage vs. noun rank')
plt.xlabel('Noun rank (most occurring)')
plt.ylabel('Percentage')
plt.savefig('graphs_nouns.eps', format='eps', dpi=800)
plt.show()

labels = 'Tweet geolocation', 'Tweet place', 'User place'
tweets = [5, 63, 4541]
explode = (0.4, 0.1, 0.1)
colors = ['red', 'yellow', 'blue']

plt.figure()
plt.title('Percentages of the tweet attributes where location is retrieved from')
plt.pie(tweets, explode=explode, autopct='%1.2f%%',
        shadow=False, startangle=90, pctdistance=1.1, labeldistance=1.3, colors= colors)
plt.legend(labels)
plt.axis('equal')
plt.savefig('pie_retriever.eps', format='eps', dpi=800)
plt.show()
