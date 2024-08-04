# Note that whenever we create normal functions within a class they are related to the instances of the class 
#  i.e the objects which are created and passed 
#  But static methods are those which :
# Static methods are defined using the @staticmethod decorator.
# They do not take the self or cls parameters.
# They can be called on the class itself or on an instance of the class.
# Static methods are useful for utility functions that are related to the class 
# but do not need to access class or instance-specific data

# It is important to know essentially that they are not classmethods which are different and are shown by using 
# decoraters
class Wars:
	name="World War 2"

	@staticmethod  # --> Decorators
	def printReq():
		print("This is WAR class ")


w1 = Wars()

print(w1.name)
Wars.printReq()
w1.name=input("Enter the name of your favourite war : ")
print(w1.name)

# Order of preference --> Instance values>>> Class values 