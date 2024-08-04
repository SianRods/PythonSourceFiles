# Question Number 1 --> Worker at Microsoft 

class Programmer : 
	#  Declaring the class Variable : 
	company="Microsoft"

	def __init__(self,name,age,yrs) :
		self.name=name
		self.age=age
		self.yrs=yrs

p1=Programmer("Sian",20,0.5)
print(p1.name)
print(p1.age)

# Class Calculator : --> Question Number 2
class Calculator:
	def __init__(self,num1,num2) :
		self.num1=num1
		self.num2=num2

# All Non -Static Methods by Default takes the Value --> Object Itself  
	def add(self,num1,num2):
		return num1+num2
		
	def squre(self,num1):
		return num1**2
	
	def sqroot(self,num1):
		if num1>0:
			return num1**0.5
		else :
			pass


# Adding a Static Method 
# Keep a note of the indentation during this thing 
	@staticmethod
	def grtHel():
		print("Hello World You are welcome to the python programming ")


c1 =Calculator(int(input("Enter any integer number : ")),int(input("Enter any integer number : ")))

print(c1.squre(223))
print(type(c1))
print(c1.sqroot(1424))
Calculator.grtHel()

# Question Number 3

class Final:
	attribute_Class="Hello"


f1 = Final()
f1.attribute_Class="Nice World"

print(f1.attribute_Class)