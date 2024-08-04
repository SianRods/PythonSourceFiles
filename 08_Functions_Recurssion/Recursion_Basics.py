# Note that in order to Successfully Execute Recursion there must be a base condition 
# fact(n) = fact(n-1)*n
# Where the program is stopped is the end condition is here it is 1

def factorial(num):
	if(num==1 or num==0):
		return 1
	else:
		return num*factorial(num-1)
	
n=int(input("Enter any Number : "))
print("The factorial of the entered number is : ",factorial(n))