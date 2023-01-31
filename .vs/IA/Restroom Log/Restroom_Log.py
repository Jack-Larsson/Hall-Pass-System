
from tkinter import *
from time import *
import SheetsScript as SS


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
        self.geometry("800x480")
        self.configure(bg='White')
        self.makeButtons()
        self.bind('<Escape>',lambda e: window.destroy())

    def makeButtons(self):
        r=0
        c=0


        for i in range(len(self.students)):
           self.students[i]= self.students[i].replace(" ", "\n")

        buttons = []

        for j in range(len(self.students)):
            buttons.append(Button(self,text = self.students[j], width = 13, height = 3, bg = "Navy", fg= "White", font=('Arial bold',9), borderwidth= 0,  command = lambda j=j: self.OpenNewWindow(self.students[j])).grid(row = r, column = c, padx = 8, pady = 8))
            c+=1
            if (c==7):
                c=0
                r+=1


    def OpenNewWindow(self, student):
        self.withdraw()
        name = student.split("\n")
        print(name[1], name[0])
        SS.printstudent(name[1], name[0])
        print(name[0])
        Thanks(self, student)
        

class Thanks(Tk):

    def __init__(self, parent, student_name):
        super().__init__()

        self.parent = parent
        self.geometry("800x480")
        #self.attributes('-fullscreen', True)
        self.configure(bg='Navy')
        Label(self, fg= "White",bg='Navy', text = "Thank You!\nHave Fun", font=('Helvetica bold',115)).grid(row=1, column= 1)
       
        #print("Thanks test"+ student_name)

        self.after(5000, lambda: self.OpenNewWindow(student_name))

        self.bind('<Escape>',lambda e: parent.destroy())

    def OpenNewWindow(self, leaver):
        self.withdraw()
        StudentOut(self, leaver)


class StudentOut(Tk):

    def __init__(self, parent, student_name):

        super().__init__()

        self.parent = parent
        self.geometry("800x480")
        #self.attributes('-fullscreen', True)

        self.configure(bg='Navy')

        #print("new screen test")

        IsOut = student_name
        IsOut = IsOut.replace("\n", " ")

        goodbye= Label(self, fg= "White",bg='Navy', text = IsOut + " \nis currently out\nThank you for\nyour patience", font=('Helvetica bold',60))
        goodbye.grid(row= 1, column=1)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)


        self.bind('<Escape>',lambda e: parent.destroy())


if __name__ == "__main__":
    window = SelectStudent()
    window.mainloop()