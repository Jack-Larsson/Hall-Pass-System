import Scanner
from Restroom_Log import Welcome
import threading

RL = Welcome()

def start_threads():
    global Startthread
    Startthread = threading.Thread(target = Scanner.scanner, args = ())

def main():
    RL.mainloop()

if __name__ == '__main__':
    start_threads()
    main()