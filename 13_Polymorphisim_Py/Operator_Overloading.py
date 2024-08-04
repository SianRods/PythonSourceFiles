# Polymorphism --> Many Forms 
#  Operator  Polymorphism --> When a Same Operator is allowed to have different meaning depending on context
#  Example 1]
print(1+2) #--> Adds two values 
# Because objects of type int have their own definition of addition operator 
print("Hello"+"World") #--> Concatenates 
# Objects of type string have their own definition of add operator
print([1,2,3]+[4,5,6]) #--> Merges Both the Lists 
# Definition for addition operator is predefined in the list class 
#  This concept is called as operator overloading 

print("Hello"*4) #--> Multiplication operator overloading incase of String

# Similar to this operator overloading can be acheived for predefined classes 