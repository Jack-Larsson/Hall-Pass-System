import mysql.connector

#create connection to DataBase
db = mysql.connector.connect(
    host = 'class-rosters.cwapanloqcsi.us-east-2.rds.amazonaws.com',
    user = 'admin',
    passwd = 'PublicEnemy1',
    database = 'StudentList'
)

#create cursor object to read through database row by row
mycursor = db.cursor()

def pullClass(period):
    #select each student who is in the same class period as the scanned tag
    mycursor.execute(f"SELECT student FROM classRosters WHERE course LIKE '{period}%'")
    #create and add to list of students in selected class period
    rawstudents = []
    for (student,) in mycursor:
        rawstudents.append(student)

    #Create and add to new list of reformatted names    
    students = []
    for string in rawstudents:
        temp_string = string.split(", ")
        new_string = temp_string[1] + " " + temp_string[0]
        students.append(new_string)
    
    return students


