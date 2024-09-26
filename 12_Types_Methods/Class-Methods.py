# Class Methods are special methods denoted using the decorator to make changes in the class attributes directly 
# which is not possible using the methods like Static and Normal ones 

#  all class methods necessarily take 'cls' as its first argument !

#  Lets Understand this using an example : -

class Car : 
	# All the below Attributes which are declared outside of all the functions are related to the class Car 
	#  And are called as class attributes 
	name ="Default "
	price = 10000000
	colour= "Blue"
	model=2024


# Note that when we create a construtor where self as the object itself is passed 
# It necessarily creates attributes which are realted to the objects rather than classes 
# however the object attributes is set using the construtor Note --> Class Attribute remains the same 
	def __init__(self,name , price,colour,model) :
		self.name=name 
		self.model=model 
		self.price=price
		self.colour=colour

# In order to access any object attribute we use --> ObjectName.Attribute
# In order to access any class Attribute we use --> ClassName.Attribute || objectname.__class__.Attribute

# Implementing a Class Method allows us to play with class attribute using the method directly 
# Each and every class method accepts class 'cls' as an implicit parameter 

	@classmethod
	def classMethodInit(cls,name,model):
		cls.name=name
		cls.model=model


# Now Lets Implement the above code to understand it better : -->
c1 = Car("Porshe",2424333,"Black",2020)
print(c1.name) # Prints the object attribute 
print(c1.__class__.name) # Prints the class Attributes 
print(Car.name)


#  Now in order to change the class attributes we can use : -->
c1.classMethodInit("Pagani",2023)
print(Car.name)

















