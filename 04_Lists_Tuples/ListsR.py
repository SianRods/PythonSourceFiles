#  Lists are Mutable Data Types in Python Unlike Tuples 
li=[12,32,2.32,"Sian"]
print(type(li))
i=0
for item in li:
	print(li[i])
	i+=1

	# Iterating Throught the Lists 

while(True):
	print("Add Element in the Lists : ")
	li.append((input("Enter : ")))
	if(li.__contains__("Exit")):
		break

# Creating a Duplicate Lists for the Given Lists : 
cpy_list=li.copy()
print(len(cpy_list))
