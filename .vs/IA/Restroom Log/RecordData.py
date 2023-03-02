from time import *
from SheetsScript import *

t = localtime()
timeout = ""
timein = ""
last = ""
first = ""

#record time student left
def TimeOut():
    global timeout
    timeout = strftime("%H:%M:%S", t)
    
#record time student returned
def TimeIn():
    global timein
    timein = strftime("%H:%M:%S", t)

#get the student that is using the hall pass   
def getStudent(lastname, firstname):
    global last, first
    last = lastname
    first = firstname

#record the student, the time they left, and the time they rturned in spreadsheet
def combine():
    TimeIn()
    printstudent(last, first, timeout, timein)
