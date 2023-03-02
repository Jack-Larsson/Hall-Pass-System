import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import RecordData as RD
from Restroom_Log import Welcome

GPIO.setwarnings(False)
reader = SimpleMFRC522()

#get info from class period and open SelectStudent window                       
def OpenClass(period):
        #get that class period for use
        Welcome.OpenSelectStudent()
        check = period+1
        print(check)

#read tag info and return class period for tag
def GetPeriod(string):
        for char in string:
                if char.isdigit():
                        digit = char
                        break
        OpenClass(int(digit))


def checkinout(string):
        #if the student is leaving record time and set tag to say they've left
        if "returned" in string:
                reader.write("out")
                GetPeriod(string)
                RD.TimeOut()
        #if the student is returning call combine() method
        if "out" in string:
                reader.write("returned")
                RD.combine()

def scanner():
        try:
                text = reader.read()
                checkinout(text)
                print(text)
               
                

        finally:
                GPIO.cleanup()


        
                
