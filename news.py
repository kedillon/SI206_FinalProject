# SI 206 Winter 2019
# Final Project
# Eva Smith

from news_info import news_api
from newsapi import NewsApiClient
import sqlite3

def news_scrape():
    api = NewsApiClient(api_key = news_api)

    conn = sqlite3.connect('Final.sqlite')
    cur = conn.cursor()
    
    cur.execute('CREATE TABLE IF NOT EXISTS News(news_outlet TEXT, author TEXT, title TEXT, description TEXT, url TEXT, publishedAt TIMESTAMP, content TEXT, UNIQUE (news_outlet, author, title, description, url, publishedAt, content))')
    
    articles = api.get_everything(q='politics', from_param='2019-03-20',
                                      to='2019-04-22') #returns dictionary
    
    num = 0
    for article in articles['articles']:
        if num >= 20:
            break
        else:
            sql = "INSERT OR IGNORE INTO News(news_outlet, author, title, description, url, publishedAt, content) VALUES (?, ?, ?, ?, ?, ?, ?)"
            # news_info = cur.fetchone()
            news_outlet = article['source']['name']
            news_author = article['author']
            news_title = article['title']
            news_description = article['description']
            news_url = article['url']
            news_publishedAt = article['publishedAt']
            news_content = article['content']
        num += 1
                # cur.execute('SELECT title FROM News WHERE title =') How to check that this doesn't equal one in table already?
                # if title is new:
        val = (news_outlet , news_author, news_title, news_description, news_url, news_publishedAt, news_content)
        cur.execute(sql, val)
        #  Use the database connection to commit the changes to the database
        conn.commit()
    
def news_vis():
    # analyzing sentiment of text;
    # compares from different sources or different search terms
    # cur.execute("SELECT * FROM news") # for news visual
    # pass content string into sentiment analyzer
    # graph sentiment of each article somehow
    pass

if __name__ == "__main__":
    news_scrape()