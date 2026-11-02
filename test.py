#age = int(input("enter age: "))
#next_year=age+1
#print("next_year you will be", next_year)
#print(float(age),str(age)+" yrs")
#print(bool(int(0)))
#agenew = input("Enter age please: ")
#print(agenew)
#print(int(agenew)/5)#

# to calc shopping bill:
# cust_name
#price of one notebook
#asking users how many notebooks they want
#convert price into float
#quantity into int
# calc bill display cust name and toatl bill

cust_name = input("Enter Customer name: ")
price_nb = int(input("Enter price of one Notebook: "))
total_nb = int(input("How many notebook to buy: "))
print("one Notebook price: " ,float(price_nb))
print("Total notebook quantity: ",int(total_nb))
print("Username: "+(cust_name)+" , ","total bill :" ,float(price_nb*total_nb))
