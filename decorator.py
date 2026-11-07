def my_decorator(func):
	def wrapper():
		print("Before Execution :")
		(func)
		print("After Execution")
		print("Completed")
	return wrapper

@my_decorator
def decfunc():
	print("test")

decfunc()

