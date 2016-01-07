import sqlite3,re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
    CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name:')
if(len(fname) < 1): fname = 'mbox.txt'
fhandle = open(fname)

for line in fhandle:
    if not (line.startswith('From: ')): continue
    pieces = line.split()
    for piece in pieces:
        orgs = re.findall('\w+@([\w.]+)', piece)
        for org in orgs:
            cur.execute('SELECT count FROM Counts WHERE org = ? ', (org.strip(), ))
            row = cur.fetchone()
            if row is None:
                cur.execute('''INSERT INTO Counts (org, count)
                        VALUES ( ?, 1 )''', ( org.strip(), ) )
            else :
                cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
                    (org.strip(), ))

conn.commit()
sql_select = 'SELECT * FROM Counts ORDER BY count DESC LIMIT 10'
print
print 'Counts:'
for row in cur.execute(sql_select):
    print str(row[0]), row[1]

cur.close()
