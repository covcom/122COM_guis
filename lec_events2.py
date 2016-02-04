import sys
from tkinter import *

class Gui:
    def __init__(self, root):
        self.root = root

        self.label = Label(self.root, \
                        text='Hello World!')
        self.label.pack()

        self.button = Button(self.root, text='Press me' , \
                        command=self.say_bye)
        self.button.pack()

    def say_bye(self):
        self.label.config(text='Bye!')

def main():
    root = Tk()
    gui = Gui(root)
    root.mainloop()

if __name__ == '__main__':
    sys.exit(main())
