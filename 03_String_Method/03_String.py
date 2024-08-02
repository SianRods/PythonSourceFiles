
# Just Like Java the Strings in Python are Immutable Data-Types 

Word = input("Enter any Word : ")\
# Now the Word is of the Data Type --> String 

SUB_WORD = Word[0:4]
# Note that --> The Last Index is not Included 
print(SUB_WORD)

# Note that String is a Data-Type in Python 
name="John Smith"
print(type(name))

# Printing only a part of the string
# Where the last Index is Excluded
print(name[2:5]) 

# Printing New Lines
print("New Line \n New Line2 ")

# Serially Printing Character of a String 
print(name[3])

# Printing characters of a String in a Reversed order 
print(name[-3])

# Multi line using three Quotes 
print("""This is a MultiLine
	  Statment""")

print("Hi my name is "+name )
word= "SeRy greEn";

# Convert all Characters to Upper Case
print(word.upper())

# Convert Characters to Lower Case
print(word.lower)

# Convert Characters First Character to Upper Case
print(word.title)

# Slicing With Skip Value --> Starting and Ending  Indexes are Assumed in case of Start and the end and Strings can be Sliced Depending upon the need 


str = input("Enter Any String : ")
print("The length of the Entered String is : ",len(str))

num1 =int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number :"))
num3 = int(input("Enter the third Number : "))	
# NEVER EVER FORGET TO TYPE CAST --> When we take a Numerical Input using input()--> Method !
print(str[num1-1:num2-1:num3-1])
