class Parent:

	def __init__(self,num1,num2) :
		print("This is the Constructor of the Parent Class")
		self.num1=num1
		self.num2=num2
		print(1+2)

class Child(Parent):

	def __init__(self,num1,num2,num3) :
		super().__init__(num1,num2)
		print("This is the constructor of the Child Class")
		self.num3=num3
		print(num3)

c1=Child(1,2,3)