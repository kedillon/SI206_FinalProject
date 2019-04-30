from NYT_info import nyt_key
from NYT_info import nyt_secret
import sqlite3
from nytimesarticle import articleAPI
import json
import requests
#import responses


def get_dict(search_terms, page = 0):
    
    data_dict = {}
    #API
    page = 0
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=' +search_terms + "&api-key=" + str(nyt_key) + "&page="+ str(page)
    
    json_data = requests.get(url, allow_redirects=False)
    json_data = json_data.json()
    data_dict[term] = json_data
    return data_dict
     

def scrape_nyt_politics(term):
    politics_dict = get_dict(term)

    if not politics_dict:
        return

    #print(politics_dict[term]['response']['docs'][0])
    # get into docs
    # if politics_dict[term] == None:
    #     return
    else:
        
        indices = [term, 'response', 'docs']

        for index in indices:
            if not politics_dict:
                return None
            politics_dict = politics_dict.get(index, None)
    
    return politics_dict
    
 

    
def politics_data(politics):

    if not politics:
        return
        #make connection to database
    conn = sqlite3.connect("Final.sqlite")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS NYT(url TEXT, headline TEXT, date TIMESTAMP, source TEXT )")
    
    #Make Sql file
    sql = "INSERT INTO NYT (url, headline, date, source) VALUES (?, ?, ?, ?)"
     
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
                value = (data["web_url"], data["headline"]["main"], data["pub_date"], data["source"])
                cur.execute(sql, value)
        #print(politics_num)


    conn.commit()
   
    

    

        
def visual_nyt(cur, terms):
    headline_count = {}
   
    for term in terms:
        cur.execute("SELECT headline FROM NYT LIMIT 20")
        for headline in cur:
            headline = headline[0].lower()
            if term in headline:
                if term in headline_count:
                    headline_count[term] += 1
                else:
                    headline_count[term] = 1
    return headline_count

def calculations_file(headline_count):
        file = open("calculations.txt", "w")
        file.write("headline_count counts the number of times the terms in search terms appear in each headline: \n")
        for term in headline_count:
            file.write("{} has {} headlines, ".format(term, headline_count[term]))
    
if __name__ == '__main__':
    #get_dict()
    
    search_terms = ['politics', 'impeach', 'election', 'immigration', 'technology', 'news', 'president', 'shooting', 'wall','trump', "america", "pelosi", 'constitution']
    for term in search_terms:
        politics_data(scrape_nyt_politics(term))
        
    conn = sqlite3.connect("Final.sqlite")
    cur = conn.cursor()
    headline_count = visual_nyt(cur,search_terms)
    calculations_file(headline_count)
