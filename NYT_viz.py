import matplotlib
import matplotlib.pyplot as plt
import sqlite3
import json


conn = sqlite3.connect("Test.sqlite")
cur = politics.cursor()
cur.execute("SELECT headline FROM NYT")
politics_dict = dict()
for news in cur:
    if news not in politics_dict:
        politics_dict[news] = 1
    else:
        politics_dict[news] += 1
        print(politics_dict)


xvals = ['Politics', 'Impeach', 'Election', 'Immigration', 'Technology', 'News', 'President', 'Shooting', 'Wall','Trump', "America", "Pelosi", 'Constitution']
yvals = [politics_dict["politics"],politics_dict["impeach"] , politics_dict["election"], politics_dict["immigration"], politics_dict["technology"], politics_dict["news"], politics_dict["president"], politics_dict["politics"],  politics_dict['shooting'], politics_dict['wall'],politics_dict['trump'], politics_dict["america"], politics_dict["pelosi"], politics_dict'constitution']]
plt.hist(xvals, yvals, align = "center")

plt.ylabel("Headline Count")
plt.xlabel("Headline Topic")
plt.title("Politics Headlines")
plt.savefig("nyt_data.png")
plt.show()