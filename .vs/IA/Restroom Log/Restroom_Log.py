
from tkinter import *
from time import *
#import SheetsScript as SS


#pi screen is 800x480 pixels
class SelectStudent(Tk):


    students =[
        "john cena",
        "mrpoopybutthole",
        "Xi jinping",
        "Lathan Lardanov",
        "Wathan Wardanov",
        "L bozo",
        "a bozo",
        "the bozo",
        "Fred",
        "Konstantin",
        "your mother",
        "malone brown",
        "lewis hamiltonn",
        "lionel pessi",
        "penaldo",
        "lakaka",
        "Alex Loser",
        "GrayGray",
        "Ken"
        "Wewis hamiltonn",
        "Wionel pessi",
        "Lenaldo",
        "Wakaka",
        "Wlex Woser",
        "WrayWray",
        "Wen",
        "lewis hamiltonn",
        "lionel pessi",
        "penaldo",
        "lakaka",
        "Alex Loser",
        "GrayGray",
        "Ken"
        "Wewis hamiltonn",
        "Wionel pessi",
        "Lenaldo",
        "Wakaka",
        "Wlex Woser",
        "WrayWray",
        "Wen",
        "john cena",
        "mrpoopybutthole",
        "Xi jinping",
        "Lathan Lardanov",
        "Wathan Wardanov",
        "L bozo",
        "a bozo",
        "the bozo",
        "Fred",
        "Konstantin"
        ]
    

    def __init__(self):
        super().__init__()
        #self.attributes('-fullscreen', True)

        frame=Frame(self)
        frame.grid(row=0,column=0, sticky = 'nw')
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        canvas=Canvas(frame,bg='Black',scrollregion=(0,0,800,628))
        canvas.config(width=800,height=480)
        canvas.grid(row=0, column=0, sticky = 'news')

        vbar=Scrollbar(frame, orient=VERTICAL)
        vbar.grid(row=0, column=1, sticky = 'nes')
        vbar.config(command=canvas.yview,
            width = 30,
            bg = 'White',
            bd = 0,
            troughcolor = 'Black'
            )
        canvas.config(yscrollcommand=vbar.set)

        self.button_frame = Frame(canvas, bg = 'Black')
        canvas.create_window((0,0), window = self.button_frame, anchor = 'nw')

        
        self.icon = PhotoImage(file = r"D:\s1649121\Documents\VS Projects\PublicEnemy1\.vs\IA\Restroom Log\GUI button.png")
        self.makeButtons()
        #self.bind('<Escape>',lambda e: window.destroy())

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
            bg = 'Black',activebackground = 'Black', width = 101, height = 76, fg= "White", font=('Microsoft YaHei UI bold',12),bd = 0,  
            command = lambda j=j: self.OpenNewWindow(self.students[j])
            ).grid(row = r, column = c, padx = 5, pady = 5))
            
            c+=1
            if (c==7):
                c=0
                r+=1 


    def OpenNewWindow(self, student):
        self.withdraw()
        name = student.split("\n")
        print(name[1], name[0])
        #SS.printstudent(name[1], name[0])
        print(name[0])
        Thanks(self, student)
        

class Thanks(Toplevel):

    def __init__(self, parent, student_name):
        super().__init__()

        self.parent = parent
        
        #self.attributes('-fullscreen', True)
        self.configure(bg='#363636')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        thank_you = Label(self, fg= "White",bg='#363636', text = "Thank You!\nHave Fun", font=('Microsoft YaHei UI bold',100))
        thank_you.grid(row=0, column=0)
        thank_you.grid_columnconfigure(1, weight=1)
        thank_you.grid_rowconfigure(1, weight=1)
        #print("Thanks test"+ student_name)

        self.after(5000, lambda: self.OpenNewWindow(student_name))

        self.bind('<Escape>',lambda e: parent.destroy())

    def OpenNewWindow(self, leaver):
        self.withdraw()
        StudentOut(self, leaver)


class StudentOut(Toplevel):

    def __init__(self, parent, student_name):

        super().__init__()

        self.parent = parent
        
        #self.attributes('-fullscreen', True)

        self.configure(bg='#363636')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #print("new screen test")

        IsOut = student_name
        IsOut = IsOut.replace("\n", " ")

        goodbye= Label(self, fg= "White",bg='#363636', text = IsOut + " \nis currently out\nThank you for\nyour patience", font=('Microsoft YaHei UI bold',60))
        goodbye.grid(row= 0, column=0)
        goodbye.grid_columnconfigure(1, weight=1)
        goodbye.grid_rowconfigure(1, weight=1)



        self.bind('<Escape>',lambda e: parent.destroy())


if __name__ == "__main__":
    window = SelectStudent()
    window.mainloop()