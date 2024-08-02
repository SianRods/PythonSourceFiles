# Dictionary is a Collection of Key-Value Pairs --> It is a type of Data Structure 

# Where the value on the left hand side denotes --> KEY
# Right hand --> 	denotes the value 

# Note that The Key-Value Pair can be of Any Data-Type and Not necessarily Strings

# Note that the main difference between using Tuples/ Lists as a Storage types and Dictionaries 
# Is that dictionaries have the ability to identify data using the key value pair 
# Hence the computational resources needed are less as compared to storing a Key_Value Pair using 
# Lists

# Presence of Commas is Also Important 

prop_prices={
	"Andheri":1.5,
	"Malad":1.0,
	"Malabar Hills":10,
	48:42

}

# Printing the Dictionaries 
print(prop_prices)

# All the Data in the Dictionaries is mutable and indexed 
print("The Prices of Property in Andheri starts at (in Cr): ")
print(prop_prices["Andheri"])
print(prop_prices[48])