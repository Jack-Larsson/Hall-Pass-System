import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import RecordData as RD
import Restroom_Log as GUI

GPIO.setwarnings(False)
reader = SimpleMFRC522()


#get info from class period and open SelectStudent window                       
def OpenClass(period):
        #get that class period for use
        GUI.Period = period
        RL.OpenSelectStudent()

#read tag info and return class period for tag
def GetPeriod(string):
        for char in string:
                if char.isdigit():
                        digit = char
                        break
        OpenClass(int(digit))


def checkinout(string):
        tag_text = string
        #if the student is leaving record time and set tag to say they've left
        if "returned" in tag_text:
                replaced = tag_text.replace("returned", "out")
                reader.write(replaced)
                RD.TimeOut()
                GetPeriod(tag_text)
                
        #if the student is returning call combine() method
        if "out" in tag_text:
                replaced = tag_text.replace("out", "returned")
                reader.write(replaced)
                RD.combine()
                GUI.Restart = True
          
                
                          
 
def scanner():
        try:
                id,text = reader.read()
                checkinout(text)
                print(text)
                print(id)          
               
        finally:
                GPIO.cleanup()
               


RL = GUI.Welcome() 
RL.mainloop()

                