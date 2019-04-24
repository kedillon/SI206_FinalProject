# Eva Smith
# SI 206: Final Project Winter 2019 -- Data Visualization
# April 23, 2019

import news from news_scrape
# from textblob import TextBlob, Word, Blobber
# from textblob.classifiers import NaiveBayesClassifier
# from textblob.taggers import NLTKTagger
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sia = SIA()
import matplotlib.pyplot as plt

class NewsSentiment:
    def __init__(self):
        #connect to database to get info
        conn = sqlite3.connect('Final.sqlite')
        cur = conn.cursor()
        #select all data from db
        cur.execute('SELECT * FROM News')
        self.info = cur.fetchall()
    def news_text_dictionary(self):
        source_dict = {}
        for row in self.info:
        
    def sentiment_calculator(text):
        # take data from table
        # split strings into list of sentences -- split on '.'
        # loop through the list of strings/sentences
            # run each string through the analyzer -- take compound value from output
            # append that number to a list
            # get average value from this list (total_sentiment/number_of_values)

        score = sia.polarity_scores()
        # analyzing sentiment of text;
        # compares from different sources or different search terms
        # cur.execute("SELECT * FROM news") # for news visual
        # pass content string into sentiment analyzer
        # graph sentiment of each article somehow
    def sentiment_lists():



if __name__ == "__main__":
    # news = Class()
    




