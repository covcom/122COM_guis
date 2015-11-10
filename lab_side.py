import sys
from tkinter import *

class Gui:
	def __init__(self, root):
		self.root = root

		self.buttonA = Button(self.root, text='A')
		self.buttonB = Button(self.root, text='B')
		self.buttonC = Button(self.root, text='C')
		self.buttonD = Button(self.root, text='D')

		self.buttonA.pack(side=TOP)
		self.buttonB.pack(side=LEFT)
		self.buttonC.pack(side=RIGHT)
		self.buttonD.pack(side=BOTTOM)

def main():
	root = Tk()
	# set the starting size of the window
	root.geometry('%dx%d' % (160,120))
	gui = Gui(root)
	root.mainloop()

if __name__ == '__main__':
	sys.exit(main())