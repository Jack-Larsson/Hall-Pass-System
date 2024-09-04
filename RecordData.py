import datetime as dt
from SheetsScript import *

timeout = ""
timein = ""
last = ""
first = ""

#record time student left
def TimeOut():
    global timeout
    now = dt.datetime.now()
    timeout = now.strftime("%H:%M:%S")
    
#record time student returned
def TimeIn():
    global timein
    now = dt.datetime.now()
    timein = now.strftime("%H:%M:%S")

#get the student that is using the hall pass   
def getStudent(lastname, firstname):
    global last, first
    last = lastname
    first = firstname

#record the student, the time they left, and the time they rturned in spreadsheet
def combine():
    TimeIn()
    printstudent(last, first, timeout, timein)
