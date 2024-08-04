# def is a keyword which is used to anounce the start of function Definition
# A function call may-be given as follows 
# function_name(any_arguments_to_be_passed)
# Any Function may also have a return type


# Note that the Function Below Does not Returns but Independtly Executes on Function Call
def patternPyramidPrint(rows):
        for i in range(0,rows):
            for j in range(0,i):
                print("*",end="")
            print("\n")
		

    
print("Enter the Number of Rows you want to print :")
rows =int(input(""))
patternPyramidPrint(rows)


# The Function Below is Returning a String hence its return type is String
def toString(name ):
     return  "Hello Mr."+name+"Welcome To Python Programming Language !"

print(toString(input("Kindly Enter your Full Name :  ")))
    


    
    