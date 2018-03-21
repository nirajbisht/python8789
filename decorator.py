def smart_divide(func):
	def inner(a,b):
		print("i am going to divide",a,'and',b)
		if b==0:
			print("whoops cannot divide")
			return
		return func(a,b)
	return inner
@smart_divide
def divide(a,b):
	return a/b
obj=divide(30,0)