import sqlite3
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class GuardianStats:
    def __init__(self):
        #open database connection
        conn = sqlite3.connect('Final.sqlite')
        cur = conn.cursor()

        cur.execute('SELECT * FROM Guardian')
        self.data = cur.fetchall()

    def stacked_bar(self):

        #list of queries made
        queries = [item[0] for item in self.data]
        sections = [item[3] for item in self.data]

        #maps queries to sections to occurrences
        map = {}
        all_sections = []

        file = open('Guardian-data.txt', 'w+')

        for i in range(len(queries)):
            query = queries[i]
            section = sections[i]

            if section not in all_sections:
                all_sections.append(section)

            if query not in map:
                map[query] = {section:1}
                file.write('query: ' + query.upper() + ' has sections:\n')

            elif section not in map[query]:
                map[query][section] = 1
                file.write(section + '\n')
            else:
                map[query][section] += 1

        file.write('\n')


        q = list(map.keys())
        labels = list(map.values())

        tups = []

        for sec in all_sections:
            tup = (map['trump'].get(sec,0), map['politics'].get(sec,0), map['brexit'].get(sec,0), map['earth'].get(sec,0), map['news'].get(sec,0), map['america'].get(sec,0), map['europe'].get(sec,0), map['immigration'].get(sec,0), map['energy'].get(sec,0), map['finance'].get(sec,0), map['economy'].get(sec,0), map['election'].get(sec,0), map['world'].get(sec,0), map['social'].get(sec,0), map['technology'].get(sec,0), map['political'].get(sec,0))
            tups.append(tup)


        plot_list = []
        plot_list.append((plt.bar(x=q, height=tups[0]),all_sections[0]))
        base = tups[0]

        for i in range(len(tups)):
            if i == 0:
                pass
            plot_list.append((plt.bar(x=q, height=tups[i], bottom=base),all_sections[i]))
            base = tuple(sum(x) for x in zip(base, tups[i]))


        plt.ylabel('Articles')
        plt.title('Article Categories by Query')
        plt.xticks(rotation=90)
        plt.legend([item[0] for item in plot_list], [item[1] for item in plot_list], loc=1, fontsize='x-small')
        plt.tight_layout()

        plt.savefig('guardian-sections')
        plt.show()



if __name__ == '__main__':
    #define a reddit object
    guard = GuardianStats()

    guard.stacked_bar()
