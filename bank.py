import random
class Bank:
	def __init__(self ,amount,wlimit):
		self.Amount=amount
		self.Wlimit=wlimit
	def register(self):
		accno=[]
		a=input("enter the  first name=")
		b=input("enter the  last name=")
		d=input("enter the  father full name=")
		age=int(input("enter the age"))
		if(age<=5):
			print("age less than six year acc.. not created")
		else:
			x=random.randint(11111111,99999999)
			print("your account no is ==",x)
			print("account created sucessfully"                                        )
	def deposit(self,n_amo):
		acc=int(input("enter the account no="))
		acname=input("enter the acc.holder name=")
		self.Amount+=n_amo
		print("amount sucessfully deposited")
		print("your current amount is=",self.Amount)
	def withdrawal(self,wamount):
		if(self.Amount-wamount<self.Wlimit):
			print("minimum withdrawal is 500")
		else:
			self.Amount-=wamount
			print("plz collect your cash=",wamount)
			print("your avilable balance is=",self.Amount)
			
b=Bank(2000,500)
while(True):
	print("1:-registration form for new account")
	print("2:-Deposit the cash")
	print("3:-Withdrawal amount")
	ch=int(input("enter the choice ="))
	if(ch==1):
		b.register()
	elif(ch==2):
		n_amo=int(input("enter the amount="))
		b.deposit(n_amo)
	elif(ch==3):
		w_amo=int(input("enter the amount="))
		b.withdrawal(w_amo)
	else:
		print("enter the valide option")
		exit()

	 