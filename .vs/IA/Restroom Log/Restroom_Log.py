
from tkinter import *
#?test
gui = Tk()
colorF = "black" 

gui.geometry("800x800")


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
    "lewis hamilsotn0",
    "lionel pessi",
    "penaldo",
    "lakaka",
    "Alex Loser",
    "GrayGray",
    "Ken"
    ]

buttons = []

for i in range(len(students)):
    students[i].replace(" ", "\n")

def position(pos):
    print(students[pos])


for j in range(len(students)):
    buttons.append(Button(gui,text = students[j], width = 10, height = 4, bg = "Blue", command = lambda j=j: position(j)).grid(row = r, column = c, padx = 10, pady = 10))
    c+=1
    if (c==5):
        c=0
        r+=1

gui.mainloop()
print("worked")
