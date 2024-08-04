# Solving problem at objects and class level just like Java 
#  Classes are the Blueprints to create objects --> Which contains attributes , methods , constructors ,etc
# In order to create an Object  we have eto Instantiate it --> and all other methods can be accessed using those objects 
# When we write class Definition --> Only Template is defined 
#  Moment we create an object --> Memory Gets Alloted


class Animal :
	name ="Default"

	def _sound_(self):
		print("It makes Sound !")

	def _legs_(self):
		print(" It has legs !")

# There is a Difference between Class Attribute and the object Attribute :
# 		1] Is the object attribute preset ?
# 		--> Yes it is preffered then 
# 		--> No 
# 		2] Is the class Attribute present ?
# 		--> Prints the class Attribute  


dog = Animal() # Object has been Created 
# dog.name="Daryl's Dog"
print(dog.name)

dog._legs_()
dog._sound_()

# if the dogs name is not initialised 