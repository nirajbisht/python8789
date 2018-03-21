lst=[34,565,68,23,65,89,213,45]
len=len(lst)
print(len)
for z in range(0,len):
	for x in range(0,len-1):
		if(lst[x]>=lst[x+1]):
			temp=lst[x]
			lst[x]=lst[x+1]
			lst[x+1]=temp
print(lst)    