n=int(input("enter number="))
lst=[]
a=[]
z=[]
c=0
b=""
m=[]
for x in range(n):
	name=(input("enter name="))
	score=(float)(input("enter grade="))
	a.append(name)
	lst.append(score)
c=sorted(lst)[1]
print(c)
print(lst[2])
for x in range(n):
	if(lst[x]==c):
		b=a[x]
		m.append(b)
print(m.sort())