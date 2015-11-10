import sys
from tkinter import *

class Gui:
	def __init__(self, root):
		self.root = root

		self.buttonA = Button(self.root, text='A')
		self.buttonB = Button(self.root, text='B')
		self.buttonC = Button(self.root, text='C')
		self.buttonD = Button(self.root, text='D')

		self.buttonA.pack(side=LEFT)
		self.buttonB.pack(side=LEFT,fill=BOTH)
		self.buttonC.pack(side=LEFT,expand=True,fill=X)
		self.buttonD.pack(side=LEFT,expand=True,fill=BOTH)

def main():
	root = Tk()
	# set the starting size of the window
	root.geometry('%dx%d' % (200,120))
	gui = Gui(root)
	root.mainloop()

if __name__ == '__main__':
	sys.exit(main())