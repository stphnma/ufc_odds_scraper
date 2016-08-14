from bs4 import BeautifulSoup
import re
from datetime import datetime
import urllib
import pandas as pd
import string

printable = set(string.printable)

URL = "https://www.bestfightodds.com/events/ufc-202-diaz-vs-mcgregor-2-1143"

soup = BeautifulSoup(urllib.urlopen(URL), 'html.parser')


odds_table = soup.findAll('table', class_ = "odds-table", recursive = True)[1]
rows = odds_table.findAll('tr')

header_row = rows[0]
bookees = dict(enumerate([x.text for x in header_row.findAll('th') if x.text != ""]))
print bookees

even_rows = odds_table.findAll('tr', {'class':'even'})
odd_rows = odds_table.findAll('tr', {'class':'odd'})

even_rows.extend(odd_rows)


data = []
for i in range(0, len(even_rows)):
    print i

    odds = [x.text for x in even_rows[i].findAll('td')]
    odds = [str(filter(lambda x: x in printable, x)) for x in odds]

    fighter = [x.text for x in even_rows[i].findAll('span', {'class':'tw'})][0]

    # print odds
    print fighter

    d = {'fighter': fighter}

    for k in bookees.keys():
        d[bookees[k]] = odds[k]

    d['timestamp'] = datetime.now()
    data.append(d)
    print "\n"

data = pd.DataFrame(data)






