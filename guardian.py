from guardian_info import key
import requests
import json
import sqlite3

def get_dict(search_term):
    dict = {}
    url = "https://content.guardianapis.com/search?q=" + search_term + "&api-key=" + key
    data = requests.get(url).json()
    return data

def guardian_scrape(search_term):

    dict = get_dict(search_term)
    articles = dict['response']['results']

    # make a connection to final project database
    conn = sqlite3.connect('Final.sqlite')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS Guardian(id TEXT, title TEXT, section TEXT, link TEXT)')

    num_added = 0

    for article in articles:
        id = str(article['id'])
        title = str(article['webTitle'])
        section = str(article['sectionName'])
        link = str(article['webUrl'])

        #if submission not already in table
        cur.execute('SELECT * FROM Guardian WHERE id = "%s"' % id)
        data = cur.fetchone()
        if data == None:
            #add to the table
            cur.execute('INSERT INTO Guardian(id, title, section, link) VALUES (?,?,?,?)', (id, title, section, link))
            num_added += 1

    conn.commit()
    print("Added", num_added, "post(s) to database!")




if __name__ == '__main__':
    guardian_scrape("trump")
