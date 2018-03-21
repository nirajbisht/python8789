from tkinter import * 
from tkinter import messagebox as tm
import pymysql
from course import Course
class Student(Frame):
	def __init__(self,obj):
		super(). __init__(obj)
		self.idLabel=Label(self,text='user id')
		self.fnameLabel=Label(self,text='first name')
		self.lnameLabel=Label(self,text='last name')
		self.fanameLabel=Label(self,text='father name')
		self.phnoLable=Label(self,text='phone no')
		self.addLable=Label(self,text='address')
		self.emailLable=Label(self,text='email')
		
		self.idEntry=Entry(self,bg='blue',fg='white')
		self.fnameEntry=Entry(self,bg='blue',fg='white')
		self.lnameEntry=Entry(self,bg='blue',fg='white')
		self.fanameEntry=Entry(self,bg='blue',fg='white')
		self.phnoEntry=Entry(self,bg='blue',fg='white')
		self.addEntry=Entry(self,bg='blue',fg='white')
		self.emailEntry=Entry(self,bg='blue',fg='white')
		
		self.addButton=Button(self, bg='blue',fg='white',text='save',command=self.save)
		self.exitButton=Button(self,bg='red',fg='white',text='exit',command=self.close)
		self.couButton=Button(self, bg='blue',fg='white',text='course',command='')
		
		self.idLabel.grid(row=0,column=0,sticky=E)
		self.idEntry.grid(row=0,column=1)
		
		self.fnameLabel.grid(row=1,column=0,sticky=E)
		self.fnameEntry.grid(row=1,column=1)
		
		self.lnameLabel.grid(row=2,column=0,sticky=E)
		self.lnameEntry.grid(row=2,column=1)
		
		self.fanameLabel.grid(row=3,column=0,sticky=E)
		self.fanameEntry.grid(row=3,column=1)
		
		self.phnoLable.grid(row=4,column=0,sticky=E )
		self.phnoEntry.grid(row=4,column=1)
		
		self.addLable.grid(row=5,column=0,sticky=E )
		self.addEntry.grid(row=5,column=1)
		
		self.emailLable.grid(row=6,column=0,sticky=E )
		self.emailEntry.grid(row=6,column=1)
		
		self.addButton.grid(row=7,column=0 )
		self.exitButton.grid(row=7,column=1)
		self.couButton.grid(row=7,column=2 )
		
		
		self.pack()
		
	def close(self):
		self.quit()
	def save(self):
		id=int(self.idEntry.get())
		first_name=self.fnameEntry.get()
		last_name=self.lnameEntry.get()
		father_name=self.fanameEntry.get()
		phno=int(self.phnoEntry.get())
		address=self.addEntry.get()
		email_id=self.emailEntry.get()
		con=pymysql.connect(db='hcl',user='root',passwd='root',host='localhost')
		cur=con.cursor()
		cur.execute(("insert into register values(%d,'%s','%s','%s',%d,'%s','%s')") %(id,first_name,last_name,father_name,phno,address,email_id))
		con.commit()
		tm.showinfo("confirmation box","record saved")
		self.idEntry.delete(0,'end')
		self.fnameEntry.delete(0,'end') 
		self.lnameEntry.delete(0,'end')
		self.fanameEntry.delete(0,'end')
		self.phnoEntry.delete(0,'end')
		self.addEntry.delete(0,'end')
		self.emailEntry.delete(0,'end')
obj=Tk()
obj.geometry("558x500")
prg=Student(obj)
obj.mainloop()
