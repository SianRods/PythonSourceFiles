
# Arithmetic Operation of Complex Numbers is best Example of Operator Overloading
class ComplexNumber :
	real=0.00 # Setting the class Attribute 
	imag = 0.00 

	def __init__(self,real,imag):
		self.real=real
		self.imag=imag

# Using the inbuilt operators
	def __add__(self,cn):
		return f"The Addition of Complex Number is {self.real+cn.real} + i{self.imag+cn.imag}"
	
c1=ComplexNumber(23,43)
c2=ComplexNumber(43,435)
print(c1.__add__(c2))