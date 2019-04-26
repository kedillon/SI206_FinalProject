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
        score_list = []
        article_count = 0
        for row in self.info:
            num_sentence = 0
            title = row[2]
            content = row[-1]
            if content != None:
                if content != "Chat with us in Facebook Messenger. Find out what's happening in the world as it unfolds.":
                    print(content)
                # split strings into list of sentences -- split on '.'
                    sentence_list = title.split('.')
                    article_count += 1
                    num_sentence = len(sentence_list)
                # run each string (loop) through the analyzer -- take compound value from output
                    for sentence in sentence_list:
                        raw_score = sia.polarity_scores(sentence)['compound'] 
                        score_list.append(raw_score)        # appending score to an overall score list
                        total = sum(score_list)
                        avg_score = total/num_sentence
                        sentiment_dict[title] = avg_score   # dictionary accumulation
                else:
                    pass
        print(sentiment_dict)
        print(len(sentiment_dict))
        # get average value from this list (total_sentiment/number_of_values)
    # get num of positive and num of negative??
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
    def sentiment_chart(self):
        pass
    def avg_length_chart(self):
        pass


if __name__ == "__main__":
    news1 = NewsSentiment()
    news1.content_sentiment_calculator()
    

