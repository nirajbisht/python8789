def fact(x):
	"""this function  for recur"""
	if(x==1):
		return 1
	else:
		return(x*fact(x-1))
y=fact(6)
print(y)
print(fact.__doc__)
