from nyt_info import nyt_key
import sqlite3
from nytimesarticle import articleAPI
import json
#import response


def scrape_nyt_politics():
    api = articleAPI(nyt_key)
    bush_dict = api.search(q="Immigration", begin_date = 20010120, end_date = 20010430)
    obama_dict = api.search(q = 'Immigration', begin_date = 20080120, end_date = 20080429)
    trump_dict = api.search(q = "Immigration", begin_date = 20160120, end_date = 20160429)
    #getting into docs
    bush = bush_dict["response"]["docs"][0]
    
    obama = obama_dict["response"]['docs'][0]
    trump = trump_dict["response"]["docs"][0]
  
   
#def database_nyt(forty_three, forty_four, forty_five):   

    #make connection to database
    conn = sqlite3.connect("NYT.sqlite")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS NYT(url Text, headline TEXT, date TEXT, source TEXT )")
    
    #Make Sql file
    sql = "INSERT INTO NYT (url, headline, date, source) VALUES (?, ?, ?, ?)"
    
    
    
    # Getting Bush Data
    bushData =(bush["web_url"], bush["headline"]["main"], bush["pub_date"], bush["source"])
    cur.execute(sql, bushData)   
    
    #Getting Obama Data
    obamaData =(obama["web_url"], obama["headline"]["main"],  obama["pub_date"], obama["source"])
    cur.execute(sql, obamaData)
    #Getting Trump Data
    trumpData = (trump['web_url'], trump["headline"]["main"], trump["pub_date"], trump["source"])
    cur.execute(sql, trumpData)
    conn.commit()
    

'''
def immigration_headline(cur):
    cur.execute("SELECT headline FROM NYT")
    headline_dict = {}
    for bushline in bushData["headline"]:
        if "Immigration" in bushline:
            if bushline not in headline
                headline_dict["Bush"] = 0
            else:
                headline_dict["Bush"] += 1
                '''
        
        


#def visual_nyt(NYT)'''
    
    
if __name__ == '__main__':
    scrape_nyt_politics()
