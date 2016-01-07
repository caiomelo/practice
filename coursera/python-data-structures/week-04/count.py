# fname = raw_input("Enter - ")
fname = "mbox-short.txt"

fh = open(fname, 'r')
count = 0

for line in fh:
    if not line.startswith("From "): continue
    words = line.rstrip().split()
    if len(words) > 0:
        count += 1
        print words[1]

print "There were", count, "lines in the file with From as the first word"