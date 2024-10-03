# Lists are Data Structure in Python which are used to store any data type within it 
list =["Sian","D098",60009230197]
print(list)

# Lists in Python are similar as that of ArrayLists in Java 

# printing the first index of the list 
print("The Size of the given list is : ",len(list))

# Python Supports List Under Lists / Nested Lists 

print(list[0])
print(list[2])

# The Size of the list can be know by passing a list object to the len() --> Function

# Majority of these Methods are useful in case of Same- Data-Types

# Methods In List --> To Manipulate 
# 1] Sorting in List  When the Data Sets are of Same-Type 
same_list=[32,42,54,6,56,656,34134,23]  #List Having the Same-Data Type 
same_list.sort()
print(same_list)

# 2]Reversing the List using Reverse Method
same_list.reverse() 
print(same_list)

# 3] Appending Data at the end of the list 

list.append("New File")

print(list)
print("The Size of the list is ",len(list))

# 4] Inserting Element at a Given Location --> Index
# Inserting an element to the Desired Position Increases the size of the list and shifts 
# each element ahead from the specified position 

list.insert(1,98)
print(list)


# 5] Deletes Element from the Specified Index --> pop()
num =int(input("Enter the index you want to delete : "))


list.pop(num)
print(list)

# 6] Removing Elements 

list.remove("Sian")
print(list)










