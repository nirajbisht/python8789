from tkinter import *
from tkinter import messagebox as tm
class Myform(Frame):
	def __init__(self,other):
		super(). __init__ (other)
		self.userlable=Label(self,text='user name')
		self.userentry=Entry(self)
		self.passentry=Entry(self,show='*')
		self.okbtn=Button(self,text="submit",command=self.show)
		self.userlable.grid(row=0,column=0)
		self.userentry.grid(row=0,column=1)
		self.okbtn.grid(columnspan=2)
		self.pack()
	def show(self):
		name=self.userentry.get()
		tm.showinfo("information",'welcome'+name)
root=Tk()
obj=Myform(root)
root.mainloop()