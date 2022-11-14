
from tkinter import *

#pi screen is 800x480 pixels
class SelectStudent:
    
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

        buttons = []

        for j in range(len(students)):
            buttons.append(Button(self.root,text = students[j], width = 10, height = 4, bg = "Blue", command = lambda j=j: self.OpenNewWindow(Thanks)).grid(row = r, column = c, padx = 10, pady = 10))
            c+=1
            if (c==5):
                c=0
                r+=1

    def OpenNewWindow(self, _class):
        self.new = Toplevel(self.root)
        _class(self.new)
        self.root.withdraw()


     

class Thanks:

    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        #self.frame = Frame(self.root)
        Label(self.root,bg = "white", fg= "blue", text = "Thank You!\nHave Fun", font=('Helvetica bold',200)).pack()
        self.root.bind('<Escape>',lambda e: root.destroy())



def main():
    root = Tk()
    app = SelectStudent(root)
    app.root.title("start")
    root.mainloop()

if __name__ == '__main__':
    main()
 