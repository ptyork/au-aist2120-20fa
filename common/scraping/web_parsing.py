# HTML
# ELEMENT is Tag + Content + Closing Tag
# <tag>TEXT</tag>
# <h1>This is the Title</h1>
# <tag attribute="value">TEXT</tag>
# <a href="http://augusta.edu">AU Website</a>

# WE NEED A PARSER
# BEAUTIFUL SOUP TO THE RESCUE
# pip install beautifulsoup4
# (or pip3 install beautifulsoup4)

# CSS SELECTOR REFERENC
# https://www.w3schools.com/cssref/css_selectors.asp

import requests
import bs4

resp = requests.get('https://en.wikipedia.org/wiki/Special:Random')
# resp = requests.get('https://en.wikipedia.org/wiki/Federal_Science_and_Technical_College_Usi-Ekiti')
resp.raise_for_status()

html_text = resp.text

# print(html_text)
soup = bs4.BeautifulSoup(html_text, features="html.parser")

# print(soup.title)
# print(soup.title.text)

h1 = soup.select_one('h1')
# print(h1)
print(h1.text)


t = soup.select_one('.infobox')    # class selector
# print(t)
# rows = t.select('tr')
rows = soup.select('.infobox tr')
for row in rows:
    # print(row.text)
    # print(len(row))
    if len(row) == 2:
        for cell in row:
            print(cell.text + ': ', end='')
        print()

