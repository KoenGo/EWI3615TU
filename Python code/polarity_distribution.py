import re
import matplotlib.pyplot as plt
import numpy as np


def gather_polarities():
    with open('datacollector_output/whole_tweet.txt', 'r', errors='ignore') as file:
        lines = file.readlines()
        polarity_list = []
        index_count = -1
        for line in lines:
            if re.search("at: (\d{2}-\d{2}-\d{4}) (\d{2}:\d{2}:\d{2})", line):
                date = re.search("at: (\d{2}-\d{2}-\d{4}) (\d{2}:\d{2}:\d{2})", line).group(0)[4:]
                if date == '14-01-2018 05:16:40':
                    return polarity_list
                polarity_list.append([date])
                index_count += 1
            if re.search("Polarity: ([- \d\.]+)", line):
                polarity_list[index_count].append(float(re.search("Polarity: ([- \d\.]+)", line).group(1)))


# hawaii missile
# Search terms at 14-01-2018 05:16:40
polarity_list = gather_polarities()
x = []
for list in polarity_list:
    x.append(list.pop(0)[11:])

del x[1::2]
del polarity_list[1::2]

x = x[:8]
polarity_list = polarity_list[:8]

print(len(x))
print(len(polarity_list))
print(x)

plt.figure(figsize=(10,7))
plt.boxplot(polarity_list)
plt.xticks(range(1,len(x)+1), x)
plt.title('Plot showing the distribution of the polarity of tweets for search terms: \'hawaii missile\' (13/01-14/01)')
plt.ylabel('Polarity')
plt.xlabel('Time')
plt.savefig('distribution_polarity.eps', format = 'eps', dpi = 800)
plt.show()

