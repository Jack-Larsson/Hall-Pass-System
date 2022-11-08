
from tkinter import *

class SelectStudent:
    
    def Students(self):
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

        for i in range(len(students)):
           students[i]= students[i].replace(" ", "\n")
        return students

    def position(pos):
        print(students[pos])
        self.OpenNewWindow()

    def OpenNewWindow(self):
        self.master.destroy()
        self.master =Tk()
        self.app = Thanks(self.master)
        self.master.mainloop()

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        r=0
        c=0

        buttons = []

        print(self.Students()[9])
       # for j in range(len(self.Students())):
       #     buttons.append(Button(self.frame,text = self.Students()[j], width = 10, height = 4, bg = "Blue", command = lambda j=j: position(j)).grid(row = r, column = c, padx = 10, pady = 10))
       #     c+=1
       #     if (c==5):
       #         c=0
       #         r+=1

class Thanks:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        Label(ByeBye, text = "Thank You!\nHave Fun").pack()



def main():
    gui = Tk()
    gui.geometry("800x800")
    app = SelectStudent(gui)
    gui.mainloop()

if __name__ == '__main__':
    main()
