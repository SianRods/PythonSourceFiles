# Types of Inheritance Supported in Python -->
#	1] Single Inheritance A-->B
# 	2] Multiple Inheritance A,B--> C
# 	3] Multilevel -Inheritance A-->B-->C

class Animal : 
	def __init__(self) :
		print("This is the Constructor of the Animal Method !")

	def sound(self):
		print("Animal Makes a Sound !")

	def eats(self):
		print("Animal Eats :)")

# Class Dog Inherits from Animal
# Syntax of Inheriting  : -
# class _nameofclass_ (_nameofinheritedclass_)

class Dog(Animal):
	def sound(self):
		print("Dog Barks ")

	def eats(self):
		print("Dogs is Non Vegetarian and Likes to eat Meat !")


class Puppy(Dog,Animal):
	def sound(self):
		print("This is a Puppy ! ")


a1=Animal()
d1=Dog()
p1=Puppy()

# a1.eats()
# p1.eats()
# p1.sound()

# OUTPUT-->
# This is the Constructor of the Animal Method !
# This is the Constructor of the Animal Method !
# This is the Constructor of the Animal Method !


# As except for animals no Constructor is defined whenever an object of the other child classes are created 
# It gives direct call to constructor of its resp parent class cause they have inherited those constructors also 


# Animal Eats :)
# Dogs is Non Vegetarian and Likes to eat Meat !
# This is a Puppy !

# Constructors have been Inherited Thats the reason Dog and puppy objects indirectly invokes the 
# constructors of the Animal class 
