# Tuple --> It is a Data Type in python 
#   It is an immutable-data type in python 

a = () # empty tuple 
b = (1,) # tuple with only one element needs a comma 
a = (1,7,2) # tuple with more than one element 
print(b)
print(type(a))

# Printing an Entire Tuple 
print(a)

str = "New String "
print(type(str))

# String , Tuples , Lists are all class in python....

# count() and index() methods in tuples 

tup =(2,2,12,324,2,424,242,'42')
print(tup)

sel=int(input("Enter the number you want to count --"))
print(tup.count(sel))

# Return the index of first occurence in the given tuple 
print("The index of the number is : 2 is ",tup.index(2))

