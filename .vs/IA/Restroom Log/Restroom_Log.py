
from tkinter import *
from time import *

#pi screen is 800x480 pixels
class SelectStudent:

    StudOut= "test student"

    students =[
        "john cena",
        "mrpoopybutthole",
        "Xi jinping",
        "Nathan mardanov",
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

    def __init__(self, root):
        self.root = root
        #self.frame = Frame(self.root)
        self.root.attributes('-fullscreen', True)
        #self.root.geometry("200x200")
        #Label(self.root, bg = "blue", text = "at least it isn't completely broken").pack
        #self.button_rename = Button(self.root, text = "New window").pack()
        self.makeButtons()
        self.root.bind('<Escape>',lambda e: root.destroy())

    def makeButtons(self):
        r=0
        c=0


        for i in range(len(self.students)):
           self.students[i]= self.students[i].replace(" ", "\n")

        buttons = []

        for j in range(len(self.students)):
            buttons.append(Button(self.root,text = self.students[j], width = 10, height = 4, bg = "Blue", command = lambda j=j: self.StudentLeaving(self.students[j])).grid(row = r, column = c, padx = 10, pady = 10))
            c+=1
            if (c==5):
                c=0
                r+=1

    def StudentLeaving(self, student):
        self.StudOut= student
        print("student leaving" +self.StudOut)
        t= Thanks(self.root)
        t.setStudent(self,student)
        self.OpenNewWindow(t)


    def OpenNewWindow(self, _class):
        self.new = Toplevel(self.root)
        _class(self.new)
        self.root.withdraw()


class Thanks:

    StudOut=""

    def __init__(self,root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        #self.frame = Frame(self.root)
        Label(self.root,bg = "white", fg= "blue", text = "Thank You!\nHave Fun", font=('Helvetica bold',200)).pack()
        self.root.bind('<Escape>',lambda e: root.destroy())
        sleep(5)
        #self.setStudent(SelectStudent.StudOut)
        print("Thanks test"+self.StudOut)
        self.OpenNewWindow(StudentOut)

    def setStudent(self, student):
        self.StudOut= student

    def OpenNewWindow(self, _class):
        self.new = Toplevel(self.root)
        _class(self.new)
        self.root.withdraw() 


class StudentOut:

    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        #self.frame = Frame(self.root)
        print("new screen test")
        print(SelectStudent.StudOut)
        Label(self.root,bg = "white", fg= "blue", text = SelectStudent.StudOut + "is currently out\nThank you for your patience", font=('Helvetica bold',100)).pack()
        self.root.bind('<Escape>',lambda e: root.destroy())


def main():
    root = Tk()
    app = SelectStudent(root)
    app.root.title("start")
    root.mainloop()

if __name__ == '__main__':
    main()
 