# Eva Smith
# SI 206: Final Project Winter 2019 -- Data Visualization
# April 23, 2019

from news import news_scrape
import nltk
import nltk.data
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sia = SIA()
import matplotlib.pyplot as plt
import sqlite3

class NewsSentiment:
    def __init__(self):
        #connect to database to get info
        conn = sqlite3.connect('Final.sqlite')
        cur = conn.cursor()
        #select all data from db
        cur.execute('SELECT * FROM News')
        self.info = cur.fetchall()
    # def news_text_dictionary(self):
    #     source_dict = {}
    #     for row in self.info:
    def title_sentiment_calculator():
        # take data from table : self.info
        overall_list = []
        for row in self.info:
            title = row[2]
            # split strings into list of sentences -- split on '.'
            sentence_list = title.split('.')
            # loop through the list of strings/sentences
            for sentence in sentence_list:
                # run each string through the analyzer -- take compound value from output
                score = sia.polarity_scores()['compound']
                print(score)
                # take compound score value from output
                # append that number to a list
        # get average value from this list (total_sentiment/number_of_values)
        
        
        # score = sia.polarity_scores()
        # analyzing sentiment of text;
        # cur.execute("SELECT * FROM news") # for news visual
        # pass content string into sentiment analyzer
        # graph sentiment of each article somehow
    def sentiment_chart():
        pass


if __name__ == "__main__":
    news1 = NewsSentiment()
    

