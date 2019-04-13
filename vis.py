from reddit import scrape_reddit_politics
import sqlite3
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_word_cloud(reddit=True):

    #open database connection
    conn = sqlite3.connect('Final.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT title FROM Reddit')
    title_list = cur.fetchall()

    all_words = []
    words_dict = {}
    for tup in title_list:
        words = tup[0].split()
        for word in words:
            word = word.rstrip('.')
            word = word.lower()

            words_dict[word] = words_dict.get(word,0) + 1
            all_words.append(word)


    wc = WordCloud(background_color="white",width=1000,height=1000, max_words=30,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(words_dict)
    plt.axis("off")
    plt.imshow(wc)
    plt.show()

    conn.commit()


if __name__ == '__main__':
    generate_word_cloud()
