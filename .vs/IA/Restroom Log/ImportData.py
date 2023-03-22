import mysql.connector

db = mysql.connector.connect(
    host = 'class-rosters.cwapanloqcsi.us-east-2.rds.amazonaws.com',
    user = 'admin',
    passwd = 'PublicEnemy1',
    database = 'StudentList'
)

mycursor = db.cursor()

def pullClass(period):
    mycursor.execute(f"SELECT student FROM classRosters WHERE course LIKE '{period}%'")
    rawstudents = []
    for (student,) in mycursor:
        rawstudents.append(student)
    students = []
    for string in rawstudents:
        temp_string = string.split(", ")
        new_string = temp_string[1] + " " + temp_string[0]
        students.append(new_string)
    print(students)
    return students
#WHERE course LIKE '[1]%'


