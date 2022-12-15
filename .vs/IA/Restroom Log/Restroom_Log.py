
from tkinter import *
from time import *


#pi screen is 800x480 pixels
#https://stackoverflow.com/questions/65527158/how-to-get-variable-from-a-class-to-another-tkinter-window
class SelectStudent(Tk):


    students =[
        "john cena",
        "mrpoopybutthole",
        "Xi jinping",
        "Nathan Mardanov",
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
        ]

    def __init__(self):
        super().__init__()
        #self.frame = Frame(self.root)
        self.attributes('-fullscreen', True)
        #self.root.geometry("200x200")
        #Label(self.root, bg = "blue", text = "at least it isn't completely broken").pack
        #self.button_rename = Button(self.root, text = "New window").pack()
        self.makeButtons()
        self.bind('<Escape>',lambda e: window.destroy())

    def makeButtons(self):
        r=0
        c=0


        for i in range(len(self.students)):
           self.students[i]= self.students[i].replace(" ", "\n")

        buttons = []

        for j in range(len(self.students)):
            buttons.append(Button(self,text = self.students[j], width = 10, height = 4, bg = "Blue", command = lambda j=j: self.OpenNewWindow(self.students[j])).grid(row = r, column = c, padx = 10, pady = 10))
            c+=1
            if (c==5):
                c=0
                r+=1


    def OpenNewWindow(self, student):
        self.withdraw()
        Thanks(self, student)
        

class Thanks(Tk):

    def __init__(self, parent, student_name):
        super().__init__()

        self.parent = parent
        self.attributes('-fullscreen', True)
        
        Label(self,bg = "white", fg= "blue", text = "Thank You!\nHave Fun", font=('Helvetica bold',200)).grid(row=1, column= 1)
       
        print("Thanks test"+ student_name)

        self.after(5000, lambda: self.OpenNewWindow(student_name))

        self.bind('<Escape>',lambda e: parent.destroy())

    def OpenNewWindow(self, leaver):
        self.withdraw()
        StudentOut(self, leaver)


class StudentOut(Tk):

    def __init__(self, parent, student_name):

        super().__init__()

        self.parent = parent
        self.attributes('-fullscreen', True)

        print("new screen test")

        Label(self,bg = "white", fg= "blue", text = student_name + " is currently out\nThank you for your patience", font=('Helvetica bold',100)).grid(row= 1, column=1)

        self.bind('<Escape>',lambda e: parent.destroy())


if __name__ == "__main__":
    window = SelectStudent()
    window.mainloop()