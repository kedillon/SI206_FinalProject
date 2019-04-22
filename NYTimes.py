from nyt_info import nyt_key
import sqlite3
from nytimesarticle import articleAPI
import json
#import response


def scrape_nyt_politics():
    api = articleAPI(nyt_key)
    politics = "politics"
    politics_dict = api.search(q = politics)
    # get into docs
    politics_data = politics_dict["response"]["docs"]
    print("!!!!!!!!!!!", politics_data[0]["headline"]["main"])
    '''
    search_term = "immigration"
    bush_dict = api.search(q= search_term, begin_date = 20010120, end_date = 20010430)
    obama_dict = api.search(q = search_term, begin_date = 20080120, end_date = 20080429)
    trump_dict = api.search(q = search_term, begin_date = 20160120, end_date = 20160429)
  
    #getting into docs
    bush = bush_dict["response"]["docs"]
    print(forty_three)
    forty_four = obama_dict["response"]['docs'][0]
    forty_five = trump_dict["response"]["docs"][0]
    print(forty_three["headline"]["main"])
  
'''
#def database_nyt(forty_three, forty_four, forty_five):   

    #make connection to database
    conn = sqlite3.connect("NYT.sqlite")
    cur = conn.cursor()
    # I think this is your problem: date should be TIMESTAMP, not TEXT
    cur.execute("CREATE TABLE IF NOT EXISTS NYT(url TEXT, headline TEXT, date TIMESTAMP, source TEXT )")
    
    #Make Sql file
    sql = "INSERT INTO NYT (url, headline, date, source) VALUES (?, ?, ?, ?)"
    
    
    # Get politics data
    politics_num = 0
    for data in politics_data:   
        if politics_num >= 20:
            pass
        else:
            politics_num += 1
            value = (data["web_url"], data["headline"]["main"], data["pub_date"], data["pub_date"])
            cur.execute(sql, value)
    conn.commit()
    # Getting Bush Data
    #bush_lst = []
    #for bush in forty_three["headline"]["main"]:
    
        #if "Immigration" in bush:
            #bush_lst.append(bush)
        #elif "immigration" in bush:
            #bush_lst.append(bush)
    

    #bush_num = 0
    #for bush_data in bush["headline"]["main"]:
        #if bush_num >= 20:
            #break
            
        #else:
            #bush_url = bush_data["web_url"]
            #bush_headline = bush_data["headline"]["main"]
            #bush_date = bush_data["pub_date"]
            #bush_source = bush_data["source"]
            #bush_num += 1
        #bushValue = bush_url, bush_headline, bush_date, bush_source
        #cur.execute(sql, bushValue)   
    


#def visual_nyt(NYT)'''
    
    
if __name__ == '__main__':
    scrape_nyt_politics()
