# Eva Smith
# SI 206: Final Project Winter 2019 -- Data Calculations & Visualization(s)
# April 23, 2019

from news import news_scrape
import nltk
import nltk.data
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sia = SIA()
import matplotlib
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
        self.sentiment_dict = {}
    def content_sentiment_calculator(self):
        # take data from table : self.info
        
        score_list = []
        article_count = 0
        for row in self.info:
            num_sentence = 0
            title = row[2]
            content = row[-1]
            if content != None:
                if content != "Chat with us in Facebook Messenger. Find out what's happening in the world as it unfolds.":
                # split strings into list of sentences -- split on '.'
                    sentence_list = title.split('.')
                    article_count += 1
                    num_sentence = len(sentence_list)
                # run each string (loop) through the analyzer -- take compound value from output
                    for sentence in sentence_list:
                        raw_score = sia.polarity_scores(sentence)['compound'] 
                        score_list.append(raw_score)        # appending score to an overall score list
                        total = sum(score_list)
                        avg_score = total/num_sentence      # get avg score for each article
                        self.sentiment_dict[title] = avg_score   # dictionary accumulation
                else:
                    pass
        return self.sentiment_dict

    def avg_article_length(self):
        # length_article_dict = {}
        # for row in self.info:
        #     art_len = len(row[-1].split())
        #     length_article_dict[row[1]].append(len)
        # maybe add the length value to another row in table??
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
        xvals = self.sentiment_dict.keys()
        yvals = self.sentiment_dict.values()
        plt.bar(xvals, yvals, align = "center")

        plt.xlabel("Article Titles")
        plt.ylabel("Average Sentiment of Article Content")
        plt.title("Average Sentiment of News Articles about Politics 2019")
        #3.Give ylabel to the plot
        plt.savefig("sentiment.png")
        plt.show()
        
    def avg_length_chart(self):
        pass


if __name__ == "__main__":
    news1 = NewsSentiment()
    news1.content_sentiment_calculator()
    news1.sentiment_chart()
    

