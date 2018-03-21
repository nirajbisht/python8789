no=(int)(input("enter the no"))
fact=0
i=2
if no==0:
	print("no is zero(0) plz enter valid number")
else:
	i=1
	while i<=10//2:
		if(no%i==0):
			fact=1
			break
		i+=1
	if fact==0:
		print(no,' is prime')
	else:
		print(no,'is not prime')
	