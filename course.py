from tkinter import * 
from tkinter import messagebox as tm
import pymysql
class Course(Frame):
	def __init__(self,obj):
		super(). __init__(obj)
		self.ccLabel=Label(self,text='course code')
		self.cnameLabel=Label(self,text='course name')
		self.cfeeLabel=Label(self,text='course fee')
		
		
		self.ccEntry=Entry(self,bg='blue',fg='white')
		self.cnameEntry=Entry(self,bg='blue',fg='white')
		self.cfeeEntry=Entry(self,bg='blue',fg='white')
		
		
		self.addButton=Button(self, bg='blue',fg='white',text='save',command=self.save)
		self.exitButton=Button(self,bg='red',fg='white',text='exit',command=self.close)
		self.couButton=Button(self, bg='blue',fg='white',text='account',command='')
		
		self.ccLabel.grid(row=0,column=0,sticky=E)
		self.ccEntry.grid(row=0,column=1)
		
		self.cnameLabel.grid(row=1,column=0,sticky=E)
		self.cnameEntry.grid(row=1,column=1)
		
		self.cfeeLabel.grid(row=2,column=0,sticky=E)
		self.cfeeEntry.grid(row=2,column=1)
		
		
		self.addButton.grid(row=3,column=0 )
		self.exitButton.grid(row=3,column=1)
		self.couButton.grid(row=3,column=2 )
		
		
		self.pack()
		
	def close(self):
		self.quit()
	def save(self):
		c_code=int(self.ccEntry.get())
		c_name=self.cnameEntry.get()
		c_fee=int(self.cfeeEntry.get())
		
		con=pymysql.connect(db='hcl',user='root',passwd='root',host='localhost')
		cur=con.cursor()
		cur.execute(("insert into course values(%d,'%s',%d)") %(c_code,c_name,c_fee))
		con.commit()
		tm.showinfo("confirmation box","record saved")
		self.ccEntry.delete(0,'end')
		self.cnameEntry.delete(0,'end') 
		self.cfeeEntry.delete(0,'end')
obj=Tk()
obj.geometry("558x500")
c=Course(obj
obj.mainloop()