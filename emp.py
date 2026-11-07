class Employee : 
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary

	def dis(self,name,salary):
		print(self.name)
		print(self.salary)

class Developer(Employee) :
	def __init__(self,name,salary,lang):
		super().__init__(name,salary)
		self.lang = lang

	def disp(self):
		self.dis(self.name,self.salary)
		print(self.lang)

dev = Developer("abhi","1000","Python")
dev.disp()