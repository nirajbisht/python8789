class Greeting:
	def __init__(self,name):
		self.name=name
	def __del__(self):
		print("Destructor started",self.name)
	def SayHello(self):
		print("Hello",self.name)
c=Greeting("neeraj")
c.SayHello()
