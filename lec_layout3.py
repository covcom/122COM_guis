import sys
from tkinter import *

class Gui:
    def __init__(self, root):
        self.root = root

        Button(self.root, text=1).pack(side=TOP)
        Button(self.root, text=2).pack(side=LEFT)
        Button(self.root, text=3).pack(side=LEFT)
        Button(self.root, text=4).pack(side=TOP)
        Button(self.root, text=5).pack(side=LEFT)
        Button(self.root, text=6).pack(side=LEFT)
        Button(self.root, text=7).pack(side=TOP)
        Button(self.root, text=8).pack(side=LEFT)
        Button(self.root, text=9).pack(side=LEFT)

def main():
    root = Tk()
    gui = Gui(root)
    root.mainloop()

if __name__ == '__main__':
    sys.exit(main())
