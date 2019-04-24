from nyt_info import nyt_key
import sqlite3
from nytimesarticle import articleAPI
import json
import requests
#import responses


def get_dict(search_terms):
    
    data_dict = {}
    #API
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=' +search_terms + "&api-key=" + str(nyt_key)
    
    json_data = requests.get(url, allow_redirects=False)
    json_data = json_data.json()
    data_dict[term] = json_data
    return data_dict
    


def scrape_nyt_politics(term):
    politics_dict = get_dict(term)
    # get into docs
    return politics_dict[term]["response"]["docs"]
    #print("!!!!!!!!!!!", politics_data)
    
 

    
def politics_data(politics):
        #make connection to database
    conn = sqlite3.connect("Final.sqlite")
    cur = conn.cursor()
    # I think this is your problem: date should be TIMESTAMP, not TEXT
    cur.execute("CREATE TABLE IF NOT EXISTS NYT(url TEXT, headline TEXT, date TIMESTAMP, source TEXT, snippet TEXT )")
    
    #Make Sql file
    sql = "INSERT INTO NYT (url, headline, date, source, snippet) VALUES (?, ?, ?, ?, ?)"
     
    politics_num = 0
    #print(len(politics_data))
    for data in politics:   
        if politics_num >= 20:
            break
        else:
            cur.execute('SELECT * FROM NYT WHERE headline = "%s"'% data['headline']['main'])
            politicsData = cur.fetchone()
            politics_num += 1
            #Check to see if politicsData not already in tagit ble
            if politicsData == None:
                #ADD TO TABLE
                value = (data["web_url"], data["headline"]["main"], data["pub_date"], data["source"],data['snippet'])
                cur.execute(sql, value)
        #print(politics_num)


                conn.commit()
   
    

    

#def visual_nyt(NYT)'''
    
    
if __name__ == '__main__':
    # get_dict()
    search_terms = ['politics', 'news', 'election', 'immigration', 'technology']
    for term in search_terms:

        politics_data(scrape_nyt_politics(term))
