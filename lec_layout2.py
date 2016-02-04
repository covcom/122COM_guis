import sys
from tkinter import *

class Gui:
    def __init__(self, root):
        self.root = root

        for i in range(1,10):
            button = Button(self.root, text=i)
            button.pack(side=LEFT)

def main():
    root = Tk()
    gui = Gui(root)
    root.mainloop()

if __name__ == '__main__':
    sys.exit(main())
