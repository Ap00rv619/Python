class Student :
	def __init__(self,name,rollnum,marks):
		self.name = name
		self.rollnum = rollnum
		self.marks = marks

	def introduce(self):
		return f"{self.name} rollnum {self.rollnum} and marks he got {self.marks}"

student1= Student("Apit","10",100)

print(student1.introduce())


class Rectangle :
	def __init__(self,len,bdt):
		self.len = len
		self.bdt = bdt

	def area(self):
		return f"{self.len * self.bdt}"

	def per(self):
		return f"Per : {2*(self.len + self.bdt)}"

Rect1 = Rectangle(10,20)
print(Rect1.area())
print(Rect1.per())

class BankAccount : 
	def __init__(self,balance):
		self.balance = balance

	def deposit(self,amt):
		self.balance+=amt
		print("Deposited:", amt)
		print("Current Balance:", self.balance)

	def withdraw(self, amt):
		if amt > self.balance:
			print("Insufficient Balance!")
		else:
			self.balance -= amt
			print("Withdrawn:", amt)
			print("Current Balance:", self.balance)


bal = BankAccount(1000)
bal.deposit(100)
bal.withdraw(200)