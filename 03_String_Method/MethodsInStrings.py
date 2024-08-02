# All the Data Types are also a Type of Classes in python which have different types of methods which can be used 

str = "GeForce-Nvidia-RTX_3050_Ti"
# Calling on the Method Capitalize on the Object String str
# Capitalises the first letter of the string 
print(str.capitalize())

if(str.endswith("i")):
	print("The Given String end with : i")
else:
	print("The String Does Not Ends with : i")

# Length of the given String : 
	print("The Size of the given String is : ",len(str))

# Counting the Occurence of a Character in a String 
print(str.count("i"))


# Replacing Characters with new ones in the String 
# Note that the characters are always enclosed within a Single Quotes 		
print(str.replace('i','*'))



# Using the Escape Sequences 

# EX] . \n endline ; \t tab sequence  ; etc  

# finding given character in string 

new="hello"
print(new.find("l"))

