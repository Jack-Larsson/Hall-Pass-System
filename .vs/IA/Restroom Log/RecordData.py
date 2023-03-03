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
    print("recoding time departed"+timeout)
    
#record time student returned
def TimeIn():
    global timein
    now = dt.datetime.now()
    timein = now.strftime("%H:%M:%S")
    print("recording time returned"+timein)

#get the student that is using the hall pass   
def getStudent(lastname, firstname):
    global last, first
    last = lastname
    first = firstname
    print("got:"+last+" "+first)

#record the student, the time they left, and the time they rturned in spreadsheet
def combine():
    TimeIn()
    print("writting to sheet")
    print(timeout)
    print(timein)
    print("writing"+last+" "+first)
    printstudent(last, first, timeout, timein)
