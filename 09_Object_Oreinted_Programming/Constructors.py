# Note that Constructors are used to initialise the objects of a class properly with certain values 
# All the methods in python which start with --> __init()__ are called as --> dunder methods 
#  'this' in java && 'self' in Python are kind of similar however 
# --> this is keyword 
# --> using self is just a Convention (PAssing the Object Itself to the Constructors and the Functions in Python as the 
# first argument)

#  Note that once you create a Constructor with certain parameters all the necessary arguments have to be passed



from typing import Any


class Car : 
	
	name ="Class Car"
	def __init__(self,name , price , Brand ) :  # Dunder Methods 
		self.name=name
		self.price=price
		self.Brand=Brand


c1 = Car("Porshe","Object Car","BrandName")

print(c1.name,c1.Brand,c1.price)

# ------------------------------------------
# By default is the object attribute is not specified each object has the class attribute and whenever 
#  the object attribute gets spcified the class attribute for that object is overwrittern
#  preference --->      Object Attribute >>> Class Attribute