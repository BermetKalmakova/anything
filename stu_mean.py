import sqlite3
import csv

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

command = "CREATE TABLE peeps_avg (id INTEGER, avg INTEGER);"
c.execute(command)

def updateAvg():
    command = "DELETE FROM courses;"
    c.execute(command)
    command = "DELETE FROM peeps_avg;"
    c.execute(command)
    filename = 'courses.csv'
    f = open(filename,'rU')
    reader = csv.DictReader(f,delimiter = ",")
    for line in reader:
        command = "INSERT INTO courses VALUES('" + line['code'] + "', " + line['mark'] + ", " + line['id'] + ")"
        c.execute(command)
    get_avg()
    
def get_avg():
    command = "SELECT COUNT(*) FROM peeps;"
    c.execute(command)
    num = int(c.fetchall()[0][0])
    for num in range(1,num+1):  
        command = "SELECT mark FROM courses WHERE id = %s;"%num
        c.execute(command)
        studentavg = 0
        list1 = c.fetchall()
        leng = len(list1)
        for each in list1:
            studentavg += each[0]
            
        command = "INSERT INTO peeps_avg VALUES (%s,%s);"%(num,studentavg/leng)
        c.execute(command)
            
        c.execute("SELECT * FROM peeps_avg;")
    print c.fetchall()
#    print studentavg/ leng

get_avg()

def addtocsv(code,mark,id):
    with open('courses.csv','a') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow([code, mark, id])

addtocsv('Science','100','5')
updateAvg()

db.commit() #save changes
db.close()  #close database
