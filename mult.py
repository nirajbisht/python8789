n=[1,3,5,6,8,9,0,9,89,34]
c=True
while(c):
	print("1:ADD")
	print("2:SEARCH")
	print("3:DELETE")
	print("4:EXIT")
	i=(int)(input("enter the command number="))
	if(i==1):
		x=input("enter the numberto be add")
		n.append(x)
		print(n)
	elif(i==2):
		el=(int)(input("enter the numberto be searched"))
		for e in n:
			if(n[e]==el):
				print("number found=",el)
	elif(i==3):
		element=(int)(input("enter the numberto be deleted"))
		n.remove(element)
		print("number is removed=",element)
	elif(i==4):
		exit()
		c=False
		print("EXIT")
	else:
		print("please enter valide input")
			