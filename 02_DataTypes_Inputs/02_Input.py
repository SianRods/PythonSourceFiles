name = input("What is your name : ")
fav_color= input("What is your fav colour : ")

print(name+"likes "+fav_color)

# It is important to note that when we take an input using the input function 
# We Store a String Literal and hence computational analysis as done with integers cant be done
# directly
# print("Enter any Random Number : ")
# rand_num=int()
# new_num = 2024-rand_num
# print(new_num)


# Converting to Type Integer Corrected Program
brth_year = input('Enter your Birth Year: ')
age = 2024-int(brth_year)
print(age)


# TYPE-CASTING into Other Data Types  --> SYNTAX
#  DATA_TYPE_TO_BE_CONVERTED(PASSED_DATA_TYPE)
# int("32")  --> String to Integer Conversion  "32"--> 32
# float(20) --> Integer to Float Conversion	   20 --> 20.0
FAV_NUMBER = input("Enter your Favourite Number : ")

# We have to Type-Cast In order to Perform Mathematical Tasks on the String Literals Recieved 