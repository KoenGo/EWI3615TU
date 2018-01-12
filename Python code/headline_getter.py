from bs4 import BeautifulSoup as bs
import requests
import re
import datetime
import os


class HeadlineGetter:
    def __init__(self):
        # Timestamp, initialize some stuff
        self.timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.stories_amount = None
        self.headlines = []
        self.make_dir()

        # Gather source code from url
        self.url = "https://news.google.com/news/headlines"
        self.source = requests.get(self.url).text
        self.get_source_code()

        # First extract top stories part from source code, then split each story and
        # write it to a separate file
        self.top_stories_to_file()
        self.split_top_stories()

        # And finally extract the headlines
        self.get_headlines()

    def __str__(self):
        return "Headlines pulled at {0}".format(self.timestamp)

    def __iter__(self):
        if self.headlines is not None:
            return iter(self.headlines)
        else:
            raise Exception("No headlines found!")

    def make_dir(self):
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, 'webscraper_output')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

    def get_source_code(self):
        self.soup = bs(self.source, 'html.parser')

        with open('webscraper_output/unformatted_source.txt', 'wb') as file:
            file.write(self.source.encode('utf-8', 'ignore'))

        with open('webscraper_output/full_source.txt', 'wb') as file:
            file.write(self.soup.prettify().encode('utf-8', 'ignore'))

    def top_stories_to_file(self):
        with open('webscraper_output/full_source.txt', 'r', errors='ignore') as file:
            lines = file.readlines()
            line_iter = iter(lines)
            line = next(line_iter)
            with open('webscraper_output/top_stories_source.txt', 'w') as chopped_file:
                while True:
                    if re.search(
                            '(\<a class="\w{6}" href="headlines/section/topic/WORLD\?ned=us" jslog="\d{5}; track: click;"\>)[^World]',
                            line):
                        break
                    chopped_file.write(line)
                    line = next(line_iter)

    def split_top_stories(self):
        with open('webscraper_output/top_stories_source.txt', 'r', errors='ignore') as file:
            lines = file.readlines()
            line_iter = iter(lines)
            line = next(line_iter)
            split_nr = 1
            while True:
                grouped_headlines_file = 'webscraper_output/headlines_{}.txt'.format(split_nr)
                with open(grouped_headlines_file, 'w') as gh_file:
                    while True:
                        if re.search('View full coverage', line):
                            split_nr += 1
                            line = next(line_iter)
                            break
                        gh_file.write(line)
                        try:
                            line = next(line_iter)
                        except StopIteration:
                            self.stories_amount = split_nr - 1
                            return
                # Avoid getting stuck in infinite loop when something goes wrong
                if split_nr > 10:
                    raise Exception("Something might be wrong here!")

    def get_headlines_from_file(self, file):
        """Automatically gets all head lines form a source file"""
        with open(file, 'r', errors='ignore') as file:
            headlines = re.findall('jsname="\w{6}" role="heading" target="_blank">([^<]+)', file.read())
        return headlines

    def get_headlines(self):
        for file_nr in range(self.stories_amount):
            file_name = "webscraper_output/headlines_{}.txt".format(file_nr + 1)
            self.headlines.append(self.get_headlines_from_file(file_name))