lst=[]
for x in range(int(input("Enter number of records: "))):
	name = input("enter name: ")
	score = float(input("enter score: "))
	lst.append([name,score])
print(lst)
s=sorted(set([i[1] for i in lst]))[1]
for i in lst:
	if[1]==s:
		print("second highest:",lst[1][0])
	else:
		break
print("\n".join(sorted([i[0] for i in lst if i[1] == s])))