import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: ')) - 1

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

for i in range(count):
    print 'Retrieving:', url
    for index, tag in enumerate(tags):
        if index == position:
            url = tag.get("href", None)
            html = urllib.urlopen(url).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            break

print "Last URL:", url