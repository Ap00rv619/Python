# create a list containing marks of 5 students, display the list and calc the total of each student and the avg of all five

marks = [
    [80, 85, 90, 75, 95],
    [70, 75, 80, 85, 90],
    [60, 65, 70, 75, 80],
    [90, 85, 95, 80, 90],
    [75, 80, 85, 90, 95]
]

total_sum = 0;

for i in range(5):
	total = sum(marks[i])
	print("Student:",i+1)
	print("Marks: ",marks[i])
	print("Total: ", total)
	total_sum = total_sum+total

class_avg = total_sum/25
print(total_sum)
print(class_avg)

# create a tuple of 10 nums, disp len, display first element, display last element, disp elements from index 2 to 6

tup = (1,2,3,4,5,6,7,8,9,10)
print(tup[0])
print(tup[-1])
print(len(tup))
print(tup[2:7])
# create a set containing 10 nos, including duplicated values,display the sets and observe how duplicated are handled

sett = {2,3,3,4,5,6,6,6,7,8}
print(len(sett))
print(sett)

#create 2 set and find union of both set
a1={10,20,30,40}
b1={30,40,50,60}
res = a1.union(b1)
print(res)

# to manage employee details and salaries using list and tuples
# create tuple containing emp id, emp name and dept
# create a list containg a salaries of 5 employees
# disp emp details, disp all salaries, calc total salary, calc avg salary, find the highest and lowest salary, add a new salary to the list and display the updated list.

emp1 = (101, "John", "HR")
emp2 = (102, "David", "IT")
emp3 = (103, "Smith", "Finance")
emp4 = (104, "Rahul", "Marketing")
emp5 = (105, "Priya", "IT")

print(emp1)
print(emp5)

sal = [10,20,30,40,50]
print(sal)
print("avg sal: ",sum(sal)/5)
print(max(sal))
print(min(sal))
sal.append(60)
print(sal)