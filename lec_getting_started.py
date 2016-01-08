import sys
from tkinter import *

def main():
	root = Tk()

	label = Label(root, text='Hello World!')
	label.pack()
	
	root.mainloop()

if __name__ == '__main__':
	sys.exit(main())