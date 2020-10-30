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

# NOTE: I'm adding in the URL of the article here...this is different than
#       the requested URL because the random article redirects to a different
#       page.
print(f"FROM: {resp.url}")

# NOTE: I'm adding in the text of the first paragraph just to provide more context.
#       The [0] index really just does the same thing as select_one...just
#       worth showing that the results of a "select" call can be indexed to find
#       a specific one. Note also that I'm doing the entire select and get text
#       part in a single statement.
print()
print(soup.select('p')[0].text)

t = soup.select_one('.infobox')    # class selector
# print(t)
# rows = t.select('tr')
rows = soup.select('.infobox tr')

# NOTE: Adding in an "escape hatch" here since not all wikipedia articles have
#       an info box table.
if len(rows) == 0:
    print("That is all.")
    exit()
else:
    print("NOTABLE FACTS")
    print("=============")

# NOTE: In class we iterated over each of the elements in the
#       each row. This worked, but was a bit of a hack and resulted
#       in a trailing ":". So here are a couple of fixes.
# for row in rows:
#     # print(row.text)
#     # print(len(row))
#     if len(row) == 2:
#         # for cell in row:
#         #     print(cell.text + ': ', end='')
#         # print()

# FIX 1: use the "tag name" of the <tr> and <td> elements that SHOULD
#        be in each of the rows. This breaks sometimes.
# for row in rows:
#     if len(row) == 2:
#         print(row.th.text + ": " + row.td.text)

# FIX 2: use the contents collection of the row to select whatever is in the
#        table. Has the benefit of working whether they use <th> and <td> or JUST
#        two <th> elements.
for row in rows:
    if len(row) == 2:
        print(row.contents[0].text + ": " + row.contents[1].text)
