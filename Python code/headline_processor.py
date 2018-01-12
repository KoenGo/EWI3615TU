import re
from textblob import TextBlob as TB
from collections import Counter
from headline_getter import HeadlineGetter
import collections


class HeadlineProcessor:
    def __init__(self):
        self.HeadlineGetter = HeadlineGetter()
        self.timestamp = self.HeadlineGetter.timestamp
        self.headlines = self.trim_headlines()
        self.search_terms = [[term for term, count in story] for story in self]

    def __str__(self):
        return self.HeadlineGetter.__str__()

    def __iter__(self):
        top_nouns_list = []
        for headline in self.headlines:
            top_nouns_list.append(self.top_nouns_per_list(headline))
        return iter(top_nouns_list)

    def trim_headlines(self):
        result = []
        for headline_group in self.HeadlineGetter:
            tmp_headline = []
            for headline in headline_group:
                tmp_headline.append(re.sub('\\n', '', headline).strip(' '))
            result.append(tmp_headline)
        return result

    def extract_nouns_sentence(self, sentence):
        if isinstance(sentence, str):
            tb_sentence = TB(self.sentence_strip_qoutes(sentence))
        else:
            raise Exception("Input must be string")
        noun_list = tb_sentence.noun_phrases

        # Sub function to flatten the output
        def flatten(l):
            for el in l:
                if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
                    yield from flatten(el)
                else:
                    yield el

        result = [i.split(" ") for i in noun_list]
        return flatten(result)

    def sentence_strip_qoutes(self, sentence):
        word_list = sentence.split(" ")
        new_list = []
        for word in word_list:
            new_list.append(word.strip("'").strip('"'))
        new_sentence = ''
        for word in new_list:
            new_sentence += ' ' + word
        return new_sentence

    def extract_nouns_list(self, list):
        result = []
        for sentence in list:
            result += (self.extract_nouns_sentence(sentence))
        return result

    def top_nouns_per_list(self, list, n=10):
        counted_nouns = Counter(self.extract_nouns_list(list)).most_common(n)
        noun_list = sorted(counted_nouns, key=lambda tuple: tuple[1], reverse=True)
        noun_list_copy = noun_list[:]
        for pair in noun_list:
            if pair[0] == ("'s" or "'ll"):
                noun_list_copy.remove(pair)
        return noun_list_copy