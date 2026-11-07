def even_num(limit):
	for i in range(2,limit+1,2):
		yield i


limit = int(input("Enter number: "))

for i in even_num(limit):
	print(i)