
from tkinter import *
from time import *
import datetime as dt
import threading
import concurrent.futures
import RecordData as RD
import Scanner as SC
import ImportData as DB

Restart = False
Period = 0

#pi screen is 800x480 pixels
class Welcome(Tk):

    def __init__(self):

        super().__init__()
        
        self.attributes('-fullscreen', True)
        print("restarted")
        self.configure(bg='#363636')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #create centerd label to welcome hall pass user
        welcomelabel = Label(self, fg= "White",bg='#363636', text = "Welcome!\nscan tag to begin", font=('Microsoft YaHei UI bold',60))
        welcomelabel.grid(row= 0, column=0)
        welcomelabel.grid_columnconfigure(1, weight=1)
        welcomelabel.grid_rowconfigure(1, weight=1)

        self.Startthread = threading.Thread(target =SC.scanner, args=())
        self.Startthread.start()
        #Startthread.join()

        self.bind('<Escape>',lambda e: self.destroy())
        
        

    def OpenSelectStudent(self):
        self.withdraw()
        SelectStudent(self)
        
    


class SelectStudent(Toplevel):

    students = []

    

    def __init__(self, parent):
        super().__init__()
        self.parent =parent
        self.students = DB.pullClass(Period)
        #creating a main frame for button window
        frame=Frame(self)
        frame.grid(row=0,column=0, sticky = 'nw')
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        #creating a canvas that can be scrolled through
        canvas=Canvas(frame,bg='Black',highlightcolor= 'Black',bd = 0,highlightthickness=0, scrollregion=(0,0,770,(len(self.students)/6)*100))
        canvas.config(width=770,height=480)
        canvas.grid(row=0, column=0, sticky = 'news')

        #create vertical scroll bar
        vbar=Scrollbar(frame, orient=VERTICAL)
        vbar.grid(row=0, column=1, sticky = 'nes')
        vbar.config(command=canvas.yview,
            width = 30,
            bg = '#363636',
            bd = 0,
            troughcolor = 'Black'
            )
        canvas.config(yscrollcommand=vbar.set)

        #create frame inside of canvas to place buttons in
        self.button_frame = Frame(canvas, bg = 'Black')
        canvas.create_window((0,0), window = self.button_frame, anchor = 'nw')

        #import image for buttons and call make button method
        self.icon = PhotoImage(file = r"/home/hanskonstantin/PublicEnemy1/.vs/IA/Restroom Log/GUIButtonV2.png")
        self.attributes('-fullscreen', True)
        self.makeButtons()

    def makeButtons(self):
        r=0
        c=0
        #seperate names into two lines to fit inside button
        for i in range(len(self.students)):
           self.students[i]= self.students[i].replace(" ", "\n")

        #create list of buttons to add to for each student
        buttons = []
        #Create grid of buttons that display and return a specific student before opening new window
        for j in range(len(self.students)):
            buttons.append(Button(self.button_frame ,text = self.students[j], image = self.icon, compound = CENTER,
            bg = 'Black',activebackground = 'Black', width= 105, height= 90, fg= "White", font=('Microsoft YaHei UI bold',12),bd = 0, highlightthickness= 0,  
            command = lambda j=j: self.OpenNewWindow(self.students[j])
            ).grid(row = r, column = c, padx = 0, pady = 5))
            
            c+=1
            if (c==6):
                c=0
                r+=1 

    #move to next window after button is pressed
    def OpenNewWindow(self, student):
        self.withdraw()
        #seperate student name into first and last and write them into the spreadsheet
        name = student.split("\n")
        print(name[1], name[0])
        RD.getStudent(name[1], name[0])
        print(name[0])
        Thanks(self, student)
        

class Thanks(Toplevel):

    def __init__(self, parent, student_name):
        super().__init__()

        self.parent = parent
        
        self.attributes('-fullscreen', True)

        #create centered label once student has completed check in process
        self.configure(bg='#363636')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        thank_you = Label(self, fg= "White",bg='#363636', text = "Thank You!\nHave Fun", font=('Microsoft YaHei UI bold',100))
        thank_you.grid(row=0, column=0)
        thank_you.grid_columnconfigure(1, weight=1)
        thank_you.grid_rowconfigure(1, weight=1)

        #after a few seconds, move to next window
        self.after(5000, lambda: self.OpenNewWindow(student_name))

        self.bind('<Escape>',lambda e: parent.destroy())

    def OpenNewWindow(self, leaver):
        self.withdraw()
        StudentOut(self, student_name = leaver)


class StudentOut(Toplevel):

    def __init__(self, parent= None, student_name = None):

        super().__init__()

        self.parent = parent
        
        self.attributes('-fullscreen', True)

        self.configure(bg='#363636')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #put student name back together in one word to be displayed
        if student_name is not None:
            IsOut = student_name.replace("\n", " ")

            #create centerd label to display the student who checked out until they return
            goodbye= Label(self, fg= "White",bg='#363636', text = IsOut + " \nis currently out.\nThank you for\nyour patience", font=('Microsoft YaHei UI bold',60))
            goodbye.grid(row= 0, column=0)
            goodbye.grid_columnconfigure(1, weight=1)
            goodbye.grid_rowconfigure(1, weight=1)
            print("wating for scan")

            self.Endthread = threading.Thread(target =SC.scanner, args=())
            #self.CheckRestart = threading.Thread(target =self.Restart, args=())
            self.Endthread.start()
            #self.Endthread.join()
            #self.CheckRestart.start()
            #self.CheckRestart.join()

            self.bind('<Escape>',lambda e: parent.destroy())
            self.Restart()
        else:
            IsOut = ""
        

    def Restart(self):
            global Restart
            if Restart:
                print("restarting")
                print(Restart)
                self.withdraw()
                self.parent.parent.parent.deiconify()
                self.parent.parent.parent.Startthread = threading.Thread(target =SC.scanner, args=())
                self.parent.parent.parent.Startthread.start()
                Restart= False
            else:
                self.after(100,self.Restart)
           
    
#if __name__ == "__main__":
   # window = Welcome()
    #window.mainloop()
    