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
    
    cur.execute('CREATE TABLE IF NOT EXISTS News(news_outlet TEXT, author TEXT, title TEXT, description TEXT, url TEXT, publishedAt TIMESTAMP, content TEXT)')
    
    articles = api.get_everything(q='politics', from_param='2019-03-26',
                                      to='2019-04-30') #returns dictionary
    num = 0
    
    for article in articles['articles']:
        if num >= 20:
            break
        else:
            news_outlet = article['source']['name']
            news_author = article['author']
            news_title = article['title']
            news_description = article['description']
            news_url = article['url']
            news_publishedAt = article['publishedAt']
            news_content = article['content']
        num += 1
    
        cur.execute('SELECT * FROM News WHERE title = "%s"' % news_title) 
        row_info = cur.fetchone()
        if row_info == None:
            #  Use the database connection to commit the changes to the database
            sql = "INSERT OR IGNORE INTO News(news_outlet, author, title, description, url, publishedAt, content) VALUES (?, ?, ?, ?, ?, ?, ?)"
            val = (news_outlet , news_author, news_title, news_description, news_url, news_publishedAt, news_content)
            cur.execute(sql, val)
        
    conn.commit()


if __name__ == "__main__":
    news_scrape()