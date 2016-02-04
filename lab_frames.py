import sys
from tkinter import *

class Gui:
    def __init__(self, root):
        self.root = root
        
        self.label = Label(self.root,text=0)
        self.label.pack(fill=BOTH,expand=True)

        self.frame = Frame(self.root,borderwidth=10,relief=GROOVE)
        self.frame.pack(fill=BOTH,expand=True)

        self.button1 = Button(self.frame, text='1')
        self.button2 = Button(self.frame, text='2')
        self.button3 = Button(self.frame, text='3')
        self.button1.pack(side=LEFT,fill=BOTH,expand=True)
        self.button2.pack(side=LEFT,fill=BOTH,expand=True)
        self.button3.pack(side=LEFT,fill=BOTH,expand=True)
        
    def button_press(self, val):
        self.label.config(text=val)

def main():
    root = Tk()
    # set the starting size of the window
    #root.geometry('%dx%d' % (320,240))
    gui = Gui(root)
    root.mainloop()

if __name__ == '__main__':
    sys.exit(main())