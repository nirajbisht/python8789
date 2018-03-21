from tkinter import *
from tkinter import messagebox as tm
import pymysql

class Project(Frame):
	def __init__(self,abc):
		super(). __init__(abc)##super call the constructor of frame class
		self.idLabel=Label(self,text='user id')
		self.passLabel=Label(self,text='password')
		self.nameLabel=Label(self,text='first name')
		self.salaryLabel=Label(self,text='salary')
		
		
		self.idEntry=Entry(self,bg='blue',fg='white')
		self.passEntry=Entry(self,bg='blue',fg='white',show='*')
		self.nameEntry=Entry(self,bg='blue',fg='white')
		self.salaryEntry=Entry(self,bg='blue',fg='white')
		
		self.addButton=Button(self, bg='blue',fg='white',text='save',command=self.save)
		self.exitButton=Button(self,bg='red',fg='white',text='exit',command=self.close)
		self.checkButton=Button(self,text='keep me login')
		
		
		
		self.idLabel.grid(row=0,column=0,sticky=E)
		self.idEntry.grid(row=0,column=1)
		
		self.passLabel.grid(row=1,column=0,sticky=E)
		self.passEntry.grid(row=1,column=1)
		
		self.nameLabel.grid(row=2,column=0,sticky=E)
		self.nameEntry.grid(row=2,column=1)
		
		self.salaryLabel.grid(row=3,column=0,sticky=E)
		self.salaryEntry.grid(row=3,column=1)
		
		self.addButton.grid(row=4,column=0,sticky=E )
		self.exitButton.grid(row=4,column=1)
		
		
		self.pack()
		
	def close(self):
		self.quit()
	def save(self):
		id=int(self.idEntry.get())
		password=self.passEntry.get()
		name=self.nameEntry.get()
		salary=int(self.salaryEntry.get())
		con=pymysql.connect(db='hcl',user='root',passwd='root',host='localhost')
		cur=con.cursor()
		cur.execute(("insert into register values(%d,'%s','%s',%d)") %(id,password,name,salary))
		con.commit()
		tm.showinfo("confirmation box","record saved")
		self.idEntry.delete(0,'end')
		self.passEntry.delete(0,'end') 
		self.nameEntry.delete(0,'end')
		self.salaryEntry.delete(0,'end')
obj=Tk()
obj.geometry("358x200")
prg=Project(obj)
obj.mainloop()
		