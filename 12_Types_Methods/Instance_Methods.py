# Instance Methods are related to the instances of the class i.e --> Objects 

class Car : 
	name ="Default "
	price = 10000000
	colour= "Blue"
	model=2024

	# Is Instance Method 
	def __init__(self,name):
		self.name=name
		
	# Instance Method 
	def printHello(self,name ):
		print(f"Hello Mr.{name}")

c1 =Car("Volswagon")


