class Empolyee:
	def reg(self):
		name=input("enter the name")
		add=input("enter the address")
		phno=int(input("enter the phon no"))
		
class Dept(Empolyee):
	def detail(self):
		print("management class")
class Account(Dept):
	def __init__(self):
		print("this is the main classs")
t=Account()
t.detail()
t.reg()

