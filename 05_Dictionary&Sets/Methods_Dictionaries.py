# There are several Methods in dictionaries which can be used to handle our data :
prop_prices={
	"Andheri":1.5,
	"Malad":1.0,
	"Malabar Hills":10,
	48:42

}

#  1] Returns All the items of the Dictionaries in a listed format "Key-Value" Pairs
print(prop_prices.items())

# 2] Only Keys of the Corresponding Dictionaries can be fetched 
print(prop_prices.keys())

# 3] Printing only Values present in the Dictionaries 
print(prop_prices.values())

# Updating the Dictionary 
# If the Passed Key Value Pair is not present in the dictionary then it gets added or else it is updated 
# Also note the Syntax of the Update Function Properly 
prop_prices.update({"Vasai":99,48:"Maharashtra"})
print(prop_prices)

# 4] Difference Between .get() --> Method and dict_name["Key_Value"] && dict_name.get("Key_Value")

print(prop_prices.get("Andheri")) #--> Absence --> Retruns String "None"
print(prop_prices["Malabar Hills"]) # Incase of Absede of the key value --> Returns an ERROR 


# 5] Clearing all the Data in the Dictionary 
prop_prices.clear()