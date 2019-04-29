# Eva Smith
# SI 206: Final Project Winter 2019 -- Data Calculations & Visualization(s)
# April 23, 2019

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
        self.raw_sia_dict = {}
        self.outlet_counts_dict = {}
        self.avg_sia_dict = {}
        self.total_articles = 0
    
    def articles_per_outlet(self):
        for row in self.info:
            outlet = row[0]
            content = row[-1]
            if content != None:
                if content != "Chat with us in Facebook Messenger. Find out what's happening in the world as it unfolds.":
                    self.outlet_counts_dict[outlet] = self.outlet_counts_dict.get(outlet, 0) + 1
                    # self.total_articles += 1

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
                    # score_list = []
                    article_score = 0
                    for sentence in sentence_list:
                        raw_score = sia.polarity_scores(sentence)['compound'] # this is the score per sentence
                        # get avg score for each article
                        # score_list.append(raw_score)        # appending score to an overall score list per article
                        article_score += raw_score
                        avg_score = article_score/num_sentence      # get avg score for each article
                        # dictionary accumulation
                        self.raw_sia_dict[news_outlet] = self.raw_sia_dict.get(news_outlet, 0) + avg_score  # dictionary accumulation: ADD scores together
                        # make a separate for loop to count the number of articles from each news_outlet --> other function
                else:
                    pass

        return self.raw_sia_dict
    
    def avg_sentiment_per_oulet(self):
        for outlet in self.raw_sia_dict:
            avg_sentiment = self.raw_sia_dict[outlet]/self.outlet_counts_dict[outlet]
            self.avg_sia_dict[outlet] = avg_sentiment

        return self.avg_sia_dict

    def calculations_write_file(self):
        f = open('sentiment_calculations.txt', 'w')
        f.write('articles_per_outlet counts the number of articles from \neach news outlet in the News table that \nwill be used in the analysis: \n\n')
        for outlet in self.outlet_counts_dict:
            f.write('{} has {} articles. \n'.format(outlet, self.outlet_counts_dict[outlet]))
        f.write('---------------------------------\n\ncontent_sentiment_calculator calculates the average \npolarity score for each article and \nadds together those for each news source from the News table: \n\n')
        for outlet in self.raw_sia_dict:
            f.write('{} has a cumulative polarity score of {}.\n'.format(outlet, self.raw_sia_dict[outlet]))
        f.write('---------------------------------\n\navg_sentiment_per_outlet calculates \nthe average polarity for each \nnews source in the News table: \n\n')
        for outlet in self.avg_sia_dict:
            f.write('{} has an average polarity score of {}.\n'.format(outlet, self.avg_sia_dict[outlet]))
        f.close()

    def sentiment_chart(self):
        # switch to scatterplot and change xvals ****
        # could create BUBBLE CHART where color correlates to news outlet, size==polarity level,
        xvals = self.avg_sia_dict.keys()
        yvals = self.avg_sia_dict.values()
        plt.bar(xvals, yvals, align="center", color =["#001049","red","#f2d372", "blue","orange", "#90a1c5", "purple", "#d64b4b", "#1e5b9f", "green", "#a1cec1", "#fb4747"])
        plt.xticks(rotation=90, fontsize=6)
        plt.yticks(fontsize=6)
        plt.xlabel("News Outlet")
        plt.ylabel("Average Polarity Score of Article Content")
        plt.title("Average Sentiment of News Articles by News Outlet")
        plt.tight_layout()
        plt.savefig("sentiment.png")

    def sentiment_scatter(self):
        x = self.avg_sia_dict.values()
        y = self.outlet_counts_dict.values()
        plt.scatter(x,y)
        plt.xticks(rotation=0)
        plt.xlabel("Average Polarity Score")
        plt.ylabel("Number of Articles")
        plt.title("Average Polarity Compared to Number of Articles")
        plt.tight_layout()
        plt.savefig("sentiment_scatter.png")    

if __name__ == "__main__":
    news1 = NewsSentiment()
    news1.articles_per_outlet()
    news1.content_sentiment_calculator()
    news1.avg_sentiment_per_oulet()
    """can uncomment code below to regenerate each plot individually or rewrite the text file"""
    # news1.sentiment_chart()  
    # news1.sentiment_scatter()
    # news1.calculations_write_file()

