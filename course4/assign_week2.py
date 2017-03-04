import sqlite3

conn = sqlite3.connect('assign_week2.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    org = email.split("@")[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()  # fetch one row into memory

    # insert the org into DB if it didn't exist
    if row is None:
        cur.execute(
            '''INSERT INTO Counts (org, count) VALUES ( ?, 1 )''', (org, ))
    # update count
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (org, ))

# This statement commits outstanding changes to disk each
# time through the loop - the program can be made faster
# by moving the commit so it runs only after the loop completes
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print "Counts:"
for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

cur.close()