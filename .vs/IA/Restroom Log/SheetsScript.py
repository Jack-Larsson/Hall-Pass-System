from time import *

t = localtime()
current_time = strftime("%H:%M:%S", t)

def printstudent(RL):
    student = RL
    student= student.replace("\n", " ")
    print(current_time + student)