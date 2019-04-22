from nyt_info import nyt_key
import sqlite3
from nytimesarticle import articleAPI
import json
#import response


def scrape_nyt_politics():
    api = articleAPI(nyt_key)
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
  

#def database_nyt(forty_three, forty_four, forty_five):   

    #make connection to database
    conn = sqlite3.connect("NYT.sqlite")
    cur = conn.cursor()
    # I think this is your problem: date should be TIMESTAMP, not TEXT
    cur.execute("CREATE TABLE IF NOT EXISTS NYT(url TEXT, headline TEXT, date TIMESTAMP, source TEXT )")
    
    #Make Sql file
    sql = "INSERT INTO NYT (url, headline, date, source) VALUES (?, ?, ?, ?)"
    
    
    
    # Getting Bush Data
'''
    bush_lst = []
    print(forty_three["headline"]["main"])
    for bush in forty_three["headline"]["main"]:
    
        if "Immigration" in bush:
            bush_lst.append(bush)
        elif "immigration" in bush:
            bush_lst.append(bush)
    print("BUSH", len(bush_lst))'''

    bush_num = 0
    for bush_data in bush:
        if bush_num >= 20:
            break
            
        else:
            bush_url = bush_data["web_url"]
            bush_headline = bush_data["headline"]["main"]
            bush_date = bush_data["pub_date"]
            bush_source = bush_data["source"]
            bush_num += 1
        bushValue = bush_url, bush_headline, bush_date, bush_source
        cur.execute(sql, bushValue)   
    
    #Getting Obama Data
    '''
    obama_num = 0
    for obama_data in obama:
        if obama_num >= 20:
            break
        else:
            obamaData =(obama_data["web_url"], obama_data["headline"]["main"],  obama_data["pub_date"], obama_data["source"])
            obama_num += 1
        cur.execute(sql, obamaData)
    #Getting Trump Data
    trump_num = 0
    for trump_data in trump:
        if trump_num >= 20:
            break
        else:
            trumpData = (trump_data['web_url'], trump_data["headline"]["main"], trump_data["pub_date"], trump_data["source"])
            trump_num +=1
        cur.execute(sql, trumpData)
'''
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
