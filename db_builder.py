import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER);"
c.execute(command)
command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"
c.execute(command)

filename = 'courses.csv'
f = open(filename,'rU')
reader = csv.DictReader(f,delimiter = ",")
for line in reader:
    command = "INSERT INTO courses VALUES('" + line['code'] + "', " + line['mark'] + ", " + line['id'] + ")"
    c.execute(command)

filename2 = 'peeps.csv'
f2 = open(filename2,'rU')
reader2 = csv.DictReader(f2,delimiter = ",")
for line in reader2:
    command = "INSERT INTO peeps VALUES('" + line['name'] + "', " + line['age'] + ", " + line['id'] + ")"
    c.execute(command)


command = "SELECT * FROM courses;"          #put SQL statement in this string
c.execute(command)    #run SQL statement
command = "SELECT * FROM peeps;"          #put SQL statement in this string
c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database
