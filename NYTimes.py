from nyt_info import nyt_key
import sqlite3
from nytimesarticle import articleAPI
import json


def scrape_nyt_politics():
    api = articleAPI(nyt_key)
    bush_dict = api.search(q="Immigration", begin_date = 20010120, end_date = 20010430)
    obama_dict = api.search(q = 'Immigration', begin_date = 20080120, end_date = 20080429)
    trump_dict = api.search(q = "Immigration", begin_date = 20160120, end_date = 20160429)
    #getting into docs
    bush = bush_dict["response"]["docs"][0]
    
    obama = obama_dict["response"]['docs'][0]
    trump = trump_dict["response"]["docs"][0]
  
   
def database_nyt(bush, obama, trump):   

    #make connection to database
    conn = sqlite3.connect("NYT.sqlite")
    cur = conn.cursor()
    cur.execute("CREATE TABLE NYT(url Text, headline TEXT, date INTEGER, source, TEXT )")
    # use a loop, the defined cursor, to execute INSERT statements, 
    #that insert the data from each admin into the correct columns in 
    # each row of the NYT database table
    sql = "INSERT INTO NYT (url, headline, date, source) VALUES (?, ?, ?, ?)"
    for bush in bush:
        bushData =(bush["web_url"], bush["headline"], bush["pub_date"], bush["source"])
        cur.execute(sql, bushData)    
    for obama in obama:
        obamaData =(obama["web_url"], obama["headline"],  obama["pub_date"], obama["source"])
        cur.execute(sql, obamaData)
    for trump in trump:
        trumpData = (trump['web_url'], trump["headline"], trump["pub_date"], trump["source"])
        cur.execute(sql, trumpData)
    conn.commit()
#def immigration_headline(cur):
    #immigration_count = 0
    #cur.execute("SELECT headline FROM NYT")
    #for headline in bushData:
        #if imm_count >= 20:


#def visual_nyt(NYT)'''
    
    
#if __name__ == '__main__':
    #scrape_nyt_politics()
