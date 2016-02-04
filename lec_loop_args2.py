import sys
from tkinter import *

class Gui:
    def __init__(self, root):
        self.root = root

        self.label = Label(self.root, \
                        text='Hello World!')
        self.label.pack()

        for i in range(1,10):
            b = Button(self.root, text=i, \
                command=lambda n=i: self.pressed_button(n))
            b.pack(side=LEFT)
        
    def pressed_button(self, number):
        self.label.config(text='Pressed %d' % number)

def main():
    root = Tk()
    gui = Gui(root)
    root.mainloop()

if __name__ == '__main__':
    sys.exit(main())