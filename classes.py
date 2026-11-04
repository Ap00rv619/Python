class Student:
	def __init__(self,name,course):
		self.name = name
		self.course = course

	def introduce(self):
		return f"{self.name} studies {self.course}"

student1= Student("Apit","Python")
student2= Student("arpit","Chatgpt")

print(student1.introduce())
print(student2.introduce())