import sqlite3

#Create the DB
connection = sqlite3.connect('emaildb.sqlite')
cur = connection.cursor()


cur.execute('DROP TABLE IF EXISTS Counts')
# Create Table named "Counts"
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

# Open and a read text file
fname = input("Enter file name: ")
if (len(fname) < 1): fname = 'mobe.txt'
fh = open(fname)

for line in fh:
    #Only pull lines that start with From:
    if not line.startswith("From: "): continue
    pieces = line.split()
    email = pieces[1]

    # This does not actually retrieve data, this just a opening and will be ready to accept data later
    cur.execute("SELECT count FROM Counts WHERE email = ?", (email,))
    
    # You can think of this as the "GET" command
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    
    connection.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

'''
Enter file name:
cwen@iupui.edu 5
zqian@umich.edu 4
david.horwitz@uct.ac.za 4
louis@media.berkeley.edu 3
gsilver@umich.edu 3
stephen.marquard@uct.ac.za 2
rjlowe@iupui.edu 2
wagnermr@iupui.edu 1
antranig@caret.cam.ac.uk 1
gopal.ramasammycook@gmail.com 1
'''