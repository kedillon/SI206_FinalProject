# Eva Smith
# SI 206: Final Project Winter 2019 -- Data Calculations & Visualization(s)
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
    def content_sentiment_calculator(self):
        # take data from table : self.info
        sentiment_dict = {}
        overall_list = []
        article_count = 0
        for row in self.info:
            title = row[2]
            content = row[-1]
            if content != None:
            # split strings into list of sentences -- split on '.'
                sentence_list = title.split('.')
                article_count += 1
            # loop through the list of strings/sentences
            score_list = []
            for sentence in sentence_list:
                # run each string through the analyzer -- take compound value from output
                score = sia.polarity_scores(sentence)['compound']
                # print(score)
                # append that number to a list & add data to dictionary
                score_list.append(score)
                sentiment_dict[title] = score
        print(sentiment_dict)
        # get average value from this list (total_sentiment/number_of_values)
        
        # could make dictionary of {title: score}
        
        # score = sia.polarity_scores()
        # analyzing sentiment of text;
        # cur.execute("SELECT * FROM news") # for news visual
        # pass content string into sentiment analyzer
        # graph sentiment of each article somehow
    def avg_article_length(self):
        '''
        outlet_length_dict = {}
        for row in self.info:
        # take length of each string of content text and split & count words
            if row[-1] != None:
                outlet_length_dict[row[1]]=
        # calculate average
        # could also put articles in dictionary with key of news_outlet &
        #   content as list of content strings --> take average length of each outlet's releases
        '''
        pass
    def sentiment_chart():
        pass
    def avg_length_chart():
        pass


if __name__ == "__main__":
    news1 = NewsSentiment()
    news1.content_sentiment_calculator()
    

