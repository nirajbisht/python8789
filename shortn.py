a=['harry','berry','tina','akriti','harsh']
lst=[37.21,37.21,37.2,41,39]
m=[]
b=[]
v=[]
f=[]
d=[]
c=sorted(lst)[1]
for x in range(5):
	if(lst[x]==c):
		b=a[x]
		v=("".join(b))
		m=[v]
		f.extend(m)
d=sorted(f)
for x in d:
	print(x)
		
  