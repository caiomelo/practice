import urllib
from bs4 import BeautifulSoup as bs

#tests
#url = "http://python-data.dr-chuck.net/comments_42.html"

#assignment
url = "http://python-data.dr-chuck.net/comments_215331.html"

html = urllib.urlopen(url).read()
soup = bs(html, 'html.parser')

tags = soup('span')
numbers = []
for tag in tags:
    if tag.contents[0]:
        numbers.append(int(tag.contents[0]))

print sum(numbers)
