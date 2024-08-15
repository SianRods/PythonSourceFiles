# Problem No.1 
num1=int(input("Enter Number 1:"))
num2=int(input("Enter Number 2:"))
num3=int(input("Enter Number 3:"))
num4=int(input("Enter Number 4:"))

# Assuming Any Number to be Maximum
# Let num4 to be max 


# Revision for Python Viva 
item=["Hello ","World ",12,32]

# The Below Loop iterates throughout the length of the list for all elements 
print(type(item))

for i in item :
	if(i==12):
		print(f"This Number is {i} ")
	else:
		print("Still Searching ....")


# Using While Loop
while (i in item !=12):
	print("Hello World the Number 12 is not found yet")
# Iterating using range function is more faster as compared through iterating through each data type 

list=['asf ',2,4,43,5,4,6,4,6,5,678,67,8,789,78,0,890,89,34,56,7]



# Using the in range function 
for i in range(len(list)):
	print(i)


# Instead using the normal iteration 
for i in list :
	print(i)