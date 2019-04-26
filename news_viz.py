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
        self.raw_sentiment_dict = {}
        self.outlet_counts_dict = {}
    
    def articles_per_outlet(self):
        total_articles = 0
        for row in self.info:
            outlet = row[0]
            content = row[-1]
            if content != None:
                if content != "Chat with us in Facebook Messenger. Find out what's happening in the world as it unfolds.":
                    self.outlet_counts_dict[outlet] = self.outlet_counts_dict.get(outlet, 0) + 1
                    total_articles += 1
        print(total_articles)
        print(self.outlet_counts_dict)
        return self.outlet_counts_dict

    def content_sentiment_calculator(self):
        # take data from table : self.info
        article_count = 0
        for row in self.info:
            num_sentence = 0
            news_outlet = row[0]
            content = row[-1]
            if content != None:
                if content != "Chat with us in Facebook Messenger. Find out what's happening in the world as it unfolds.":
                # split strings into list of sentences -- split on '.'
                    sentence_list = content.split('.') # split content into sentences
                    article_count += 1
                    num_sentence = len(sentence_list)
                # run each string (loop) through the analyzer -- take compound value from output
                    score_list = []
                    for sentence in sentence_list:
                        raw_score = sia.polarity_scores(sentence)['compound'] # this is the score per sentence
                        # get avg score for each article
                        score_list.append(raw_score)        # appending score to an overall score list per article
                        total = sum(score_list)
                        avg_score = total/num_sentence      # get avg score for each article
                        # dictionary accumulation
                        self.raw_sentiment_dict[news_outlet] = self.raw_sentiment_dict.get(news_outlet, 0) + avg_score  # dictionary accumulation: ADD scores together
                        # make a separate for loop to count the number of articles from each news_outlet
                else:
                    pass
        print(self.raw_sentiment_dict)
        return self.raw_sentiment_dict

        # *** IDEA: bubble chart possibly where color correlates to news outlet, size==polarity level,

    def sentiment_chart(self):
        # switch to scatterplot and change xvals ****
        xvals = self.sentiment_dict.keys()
        yvals = self.sentiment_dict.values()
        plt.bar(xvals, yvals)
        plt.xticks(rotation=45)
        plt.xlabel("Articles Polarity")
        plt.ylabel("Average Sentiment of Article Content")
        plt.title("Average Sentiment of News Articles by News Outlet")
        plt.savefig("sentiment.png")
        plt.show()
        
    def avg_length_chart(self):
        pass

if __name__ == "__main__":
    news1 = NewsSentiment()
    news1.articles_per_outlet()
    news1.content_sentiment_calculator()
    # news1.sentiment_chart()
    # news1.article_counts()
    # news1.avg_article_length()
    

