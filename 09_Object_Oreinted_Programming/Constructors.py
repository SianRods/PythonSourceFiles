# Note that Constructors are used to initialise the objects of a class properly with certain values 
# All the methods in python which start with --> __init()__ are called as --> dunder methods 
#  'this' in java && 'self' in Python are kind of similar however 
# --> this is keyword 
# --> using self is just a Convention 

#  Note that once you create a Constructor with certain parameters all the necessary arguments have to be passed



from typing import Any


class Car : 
	

	def __init__(self,name , price , Brand ) :  # Dunder Methods 
		self.name=name
		self.price=price
		self.Brand=Brand


c1 = Car("Porshe",1300000,"BrandName")

print(c1.name,c1.Brand,c1.price)