fname = raw_input("Enter - ")
fname = "../week-04/mbox-short.txt"

fh = open(fname, 'r')
senders = dict()

for line in fh:
    if not line.startswith("From "): continue
    words = line.rstrip().split()
    if len(words) > 0:
        if words[1]:
            senders[words[1]] = senders.get(words[1], 0) + 1

maxSender = None
maxCount = None

for sender, count in senders.items():
    print sender, count
    if maxSender == None or count > maxCount:
        maxSender = sender
        maxCount = count

print "Sender:", maxSender
print "Count:", maxCount