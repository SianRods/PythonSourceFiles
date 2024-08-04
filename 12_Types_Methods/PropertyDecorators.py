# Propert Decorators --> It is a Decorator which is used on any method to use it as a property 
# Why the need of property decorator -->
# We are Finding the Pricing Solution of a Car Depending on its Model --> Using Dictionary
class Car : 
	name ="Default "
	price = 10000000
	colour= "Blue"
	# Defining a dictionary to adjust the Multiplicative Factor Depending Upon the Model Year : 
	modelDict ={
		2024:4,
		2023:3,
		2022:2,
		2021:1
	}

	def __init__(self,model) :
		self.model=model
		print("Your car is manufactured in the year : ",model)
		# Calculating the Price --> in the Constuctor itself 
	
	@property
	def ModelPricing(self):
		self.price= Car.price*Car.modelDict.get(self.model)
		return self.price
	
c1 = Car(2024)
print(c1.ModelPricing)
# Now Consider a Senario where i had inputted a wrong model 
# So i change it now 
c1.model=2022
# Now printing the price of self again after correcting the model year 
print(c1.ModelPricing) # This does not change the value because it is set during object creation so we have to use 

# create new Funtion to calculate price seperatley or just use the Property Decorator 

# Function can be made as property --> Automatic change wothout individually changing all the values 

