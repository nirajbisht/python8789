class Ab:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):#return object  value
		return"{0},{1}".format(self.x=x,self.y=y
	def __add__(self,other):#method overloading
		x1=self.x+self.x
		y1=self.y+self.y
		return (x1,y1)
ob1=Ab(2,4)
ab2=Ab(3,4)
print(ob1)
print(ob2)
print(ob1+ob2)