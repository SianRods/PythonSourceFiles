
    
def patternPyramidPrint(rows):
        for i in range(0,rows):
            for j in range(0,i):
                print("*",end="")
            print("\n")
		

    
print("Enter the Number of Rows you want to print :")
rows =int(input(""))
patternPyramidPrint(rows)
    
# def is a keyword which is used to anounce the start of function Definition
# A function call may-be given as follows 
# function_name(any_arguments_to_be_passed)
# Any Function may also have a return type


    
    