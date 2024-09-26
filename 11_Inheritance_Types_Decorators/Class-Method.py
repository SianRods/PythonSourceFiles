# Class Method --> A Method Which is bound to the class rather than instance/object of the same class 
# Syntax-->
# @classmethod
# def _classMethodName_(cls,para1,para2,....):
# 	print(cls._classattribute) # Prints the class Attribute
# Where cls is used to denote the class 

class Parent :
    name="DefaultName"
    constantClass = 3.14

    @staticmethod #--> related to the class doesn't accept cls, self as an valid argument 
    def statm(newConstant):
        constantClass=newConstant
        print("This is a Static Method")

    
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    @classmethod
    def classVar(cls,newConstant):
        print("The value of the new constant to be passed is : ",newConstant)
        cls.constantClass=newConstant
        print("This is a Class Method")
        

p1=Parent("Prakash",53)
print(Parent.name)

print("The value of constantCLass variable before ",Parent.constantClass)

# p1.statm(Parent,21) #--> Can't change the value of the class attribute using the static method
p1.classVar(21)

print(Parent.constantClass)