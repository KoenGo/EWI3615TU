import re
from textblob import TextBlob as TB
from collections import Counter
from headline_getter import HeadlineGetter



class HeadlineProcessor:
    def __init__(self, HeadlineGetter):
        self.HeadlineGetter = HeadlineGetter
        self.timestamp = self.HeadlineGetter.timestamp
        self.headlines = self.trim_headlines()


    def __str__(self):
        pass

    def __iter__(self):
        if self.headlines:
            return self
        else:
            raise Exception('Headlines are empty!')

    def __next__(self):
        headlines_iterator = iter(self.headlines)
        return self.top_nouns_per_list(next(headlines_iterator))

    def trim_headlines(self):
        result = []
        for headline_group in self.HeadlineGetter:
            tmp_headline = []
            for headline in headline_group:
                tmp_headline.append(re.sub('\\n','', headline).strip(' '))
            result.append(tmp_headline)
        return result

    def extract_nouns_sentence(self, sentence):
        if isinstance(sentence, str):
            tb_sentence = TB(sentence)
        else:
            raise Exception("Input must be string")
        noun_list = tb_sentence.noun_phrases
        return [i.split(" ") for i in noun_list]

    def extract_nouns_list(self, list):
        result = []
        for sentence in list:
            result += (self.extract_nouns_sentence(sentence))
        return result

    def top_nouns_per_list(self, list, n = 5):
        counted_nouns = Counter(self.extract_nouns_list(list)).most_common(n)
        return sorted(counted_nouns, key = lambda tuple: tuple[1], reverse=True)



a = HeadlineGetter()
b = HeadlineProcessor(a)
print(b.headlines)
for i in b:
    print(i)