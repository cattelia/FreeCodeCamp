import json
import sqlite3

# The "file handle" to the DB
conn = sqlite3.connect('rosterdbA.sqlite')
cur = conn.cursor()

#Delete existing tables (if they exist) and create
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
Drop table if exists Stuff;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);
                  
create table Stuff (
    id  integer PRIMARY KEY UNIQUE,
    stuff_id text);

INSERT INTO Stuff (id, stuff_id) VALUES (0, 'Student');

INSERT INTO Stuff (id, stuff_id) VALUES (1, 'Teacher')
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    
    name = entry[0]  #Name
    title = entry[1] #Course
    role = entry[2]  #Role

    #print((name, title))

    #OR IGNORE, is here to stop this from "blowing up" if this insert were to cause an error.
    #Just ignore it.

    #Name
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]
    #Course
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    #INSERT OR REPLACE, if there is a duplicate, this becomes an update statement
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ?)''',
        (user_id, course_id, role ) )


    conn.commit()

sqlstr = '''select User.id, User.name, Course.title, Stuff.stuff_id 
from User join Course join Member join Stuff
on Course.id = Member.course_id and User.id = Member.user_id and Stuff.id = Member.role'''

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1], row[2], row[3])