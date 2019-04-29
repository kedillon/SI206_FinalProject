import matplotlib
import matplotlib.pyplot as plt
import sqlite3
#import json

class NYT_data():
    def __init__(self):
        conn = sqlite3.connect("Test.sqlite")
        cur = conn.cursor()
        cur.execute("SELECT * FROM NYT")
        self.data = cur.fetchall()
        
    
    def get_dict(self):
        search_terms = ['politics', 'impeach', 'election', 'immigration', 'technology', 'news', 'president', 'shooting', 'wall','trump', "america", "pelosi", 'constitution']
        term_dict = dict()
        for term in search_terms:
            for tup in self.data:
                headline = tup[1].lower()
                if term in headline:
            #for term in search_terms:
                #if term not in self.politics_dict:
                    term_dict[term] = term_dict.get(term, 0) +1
                  
        print(term_dict)
        return term_dict

    def bar_chart(self):
        politics_dict = self.get_dict()
        xvals = ('politics', 'impeach', 'election', 'immigration', 'technology', 'news', 'president', 'shooting', 'wall','trump', "america", "pelosi", 'constitution')
        yvals = (politics_dict["politics"],politics_dict["impeach"], politics_dict["election"], politics_dict["immigration"], politics_dict["technology"], politics_dict["news"], politics_dict["president"], politics_dict["shooting"], politics_dict["wall"],politics_dict["trump"], politics_dict["america"], politics_dict["pelosi"], politics_dict["constitution"])
        plt.bar(xvals, yvals, align = "center", color = "blue")
        plt.xticks(list(xvals), rotation = 90)
        plt.xlabel("Headline Topic")
        plt.ylabel("Headline Count")
        plt.title("Politics Headlines")
        plt.tight_layout()
        plt.savefig("nyt_data.png")
        plt.show()
    

if __name__ == '__main__':
    NYT = NYT_data()
    #d = NYT.get_dict()
    NYT.bar_chart()