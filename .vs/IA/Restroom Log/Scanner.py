import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import RecordData as RD
from Restroom_Log import Welcome
from Restroom_Log import StudentOut
import threading

GPIO.setwarnings(False)
reader = SimpleMFRC522()
restart = False 


#get info from class period and open SelectStudent window                       
def OpenClass(period):
        #get that class period for use
        #try:
        RL.OpenSelectStudent()
        #except RuntimeError:
         #       restartRL.OpenSelectStudent()
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
        tag_text = string
        global restart
        global restartRL
        print("checkin/out")
        #if the student is leaving record time and set tag to say they've left
        if "returned" in tag_text:
                restart = False
                print("got returned")
                replaced = tag_text.replace("returned", "out")
                reader.write(replaced)
                print("wrte to tag:"+ replaced)
                RD.TimeOut()
                GetPeriod(tag_text)
                #Startthread.join()

        #if the student is returning call combine() method
        if "out" in tag_text:
                restart = True
                replaced = tag_text.replace("out", "returned")
                reader.write(replaced)
                print(restart)
                print("replaced text with "+ replaced)
                RD.combine()
                
                SO.withdraw()
                SO.withdraw()
                RL.deiconify()
                Startthread = threading.Thread(target = scanner, args=())
                Startthread.start()
                #RL.quit()
                #restartRL= Welcome()
                #RL = Welcome()
                #RL.mainloop()
        #return restart
                
                          
 
def scanner():
        try:
                id,text = reader.read()
                checkinout(text)
                        #return True
                start_threads()
                print(text)
                print(id)
                #return False
               
        finally:
                GPIO.cleanup()
                #return False

RL = Welcome() 
SO = StudentOut()
RL.mainloop()

                
