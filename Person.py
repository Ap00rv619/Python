class Shape :
	def __init__(self):
		pass

class Circle(Shape) : 
	def __init__(self,r):
		self.r = r

	def area(self):
		return 3.14*self.r*self.r


c = Circle(5)
print(c.area())

