print("complete report : ")
name = input("Name : ")
print(name)
expense = []
for i in range(5):
	exp = int(input("Enter Expense : "))
	expense.append(exp)

print("Total Expense :" + str(sum(expense)))
print("Avg Expense :" + str(float(sum(expense)/5)))
print("Max Expense :" + str(max(expense)))
print("Min Expense :" + str(min(expense)))

cat = ("food","education","shopping","Bills","education")
print(cat)
expset = {2,6,6,4,32,3,1,2,5,6}
print(expset)


