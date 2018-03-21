from tkinter import *
root=Tk()
def leftclick(event):
	print("left")
def middleclick(event):
	print("middle")
def rightclick(event):
	print("right")
frame=Frame(root,width=300,height=250)

frame.bind("<Frame>",leftclick) 
frame.bind("<Frame>",middleclick)
frame.bind("<Frame>",rightclick)
frame.pack()
root.mainloop()