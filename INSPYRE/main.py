from tkinter import Frame,Tk

class Window(Frame):
	def __init__(self, window):
		Frame.__init__(self)

root = Tk()
App = Window(root)
root.mainloop()