# 1] Program to Add Two Numbers
num1 = input("Enter first Number : ")
num2 = input("Enter the Second Number ")

# Type Casting the Data 


print(int(num1)+int(num2))

# 2] Remainder When Divided By --> 2

num3 =input("Enter the Number you want to Check : ")
num3 = float(num3)

rem = num3%2
print("The number when Divided by 2 leaves the remainder : %f"%rem)


# Knowledge of Data Types Formatting for print() function is necessary

# 3] Type of Variable Assigned using the input function 

sol = input("Enter type :")
print(type(sol))

a = input("Enter the First Number : ")
b = input("Enter the Second Number : ")

a= int(a)
b = int(b)


if(a>b):
	print("A is Greater than B ")
else:
	print("B is Greater then A ")

# 4] Square Of A Number : 

num_sqr=input("Enter any number : ")
num_sqr=int(num_sqr)

print("The Square of the number :",(num_sqr*num_sqr))