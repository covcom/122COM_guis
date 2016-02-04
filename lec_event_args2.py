import sys
from tkinter import *

class Gui:
    def __init__(self, root):
        self.root = root

        self.label = Label(self.root, \
                        text='Hello World!')
        self.label.pack()

        Button(self.root, text='1', \
            command=self.pressed_button(1)).pack(side=LEFT)
        Button(self.root, text='2', \
            command=self.pressed_button(2)).pack(side=LEFT)

    def pressed_button(self, number):
        self.label.config(text='Pressed %d' % number)

def main():
    root = Tk()
    gui = Gui(root)
    root.mainloop()

if __name__ == '__main__':
    sys.exit(main())