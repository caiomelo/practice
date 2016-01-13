import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter xml address: ')
# if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_42.xml"
if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_215328.xml"

xml = urllib.urlopen(url).read()
tree = ET.fromstring(xml)
counts = tree.findall(".//count")

numbers = list()

for item in counts:
    number = int(item.text)
    numbers.append(number)

print "Number of counts", len(numbers)
print "Comments sum", sum(numbers)