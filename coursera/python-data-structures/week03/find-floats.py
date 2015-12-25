import re
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        found = re.search('[0-9]+\.[0-9]+', line)
        if not (found is None):
            total += float(found.group())

try:
    average = total/count
    print "Average spam confidence:", average
except:
    print "No matches found"