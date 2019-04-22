from nyt_info import nyt_key
import sqlite3
from nytimesarticle import articleAPI
import json
import requests
#import response


def get_dict():
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=politics&api-key=' + str(nyt_key)
    json_data = requests.get(url, allow_redirects=False)
    json_data = json_data.json()
    
    return json_data


def scrape_nyt_politics():
    politics_dict = get_dict()
    # get into docs
    politics_data = politics_dict["response"]["docs"]
    print("!!!!!!!!!!!", politics_data[0]["headline"]["main"])
    
#def database_nyt(forty_three, forty_four, forty_five):   

    #make connection to database
    conn = sqlite3.connect("Final.sqlite")
    cur = conn.cursor()
    # I think this is your problem: date should be TIMESTAMP, not TEXT
    cur.execute("CREATE TABLE IF NOT EXISTS NYT(url TEXT, headline TEXT, date TIMESTAMP, source TEXT )")
    
    #Make Sql file
    sql = "INSERT INTO NYT (url, headline, date, source) VALUES (?, ?, ?, ?)"
    
    
    # Get politics data
    politics_num = 0
    print(len(politics_data))
    for data in politics_data:   
        if politics_num >= 20:
            break
        else:
            cur.execute('SELECT * FROM NYT WHERE headline = "%s"'% data['headline']['main'])
            politicsData = cur.fetchone()
            politics_num += 1
            #Check to see if politicsData not already in tagit ble
            if politicsData == None:
                #ADD TO TABLE
                value = (data["web_url"], data["headline"]["main"], data["pub_date"], data["pub_date"])
                cur.execute(sql, value)
        print(politics_num)


    conn.commit()
   
    

    

#def visual_nyt(NYT)'''
    
    
if __name__ == '__main__':
    #get_dict()
    scrape_nyt_politics()
