fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname, 'r')
count = 0
lines = fh.read()
for line in lines:
    print line
    print line.startswith('From ')
	# if not line.startswith("From "): continue
	# words = line.split()
	# print words[1]
	# count += count

print "There were", count, "lines in the file with From as the first word"