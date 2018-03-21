myset=set()

lst1=[]
n=(int)(input("enter range"))
for x in range(n):
	v=(int)(input("enter the number"))
	myset.add(v)
print(myset)
for i in myset:
	lst1.append(i)	
print(lst1)