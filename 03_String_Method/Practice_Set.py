#  1] String Concatenatioin

name = input("Enter your Name : ")
print(name+" Good Afternoon")

# 2] Letter Formatting 
letter = '''Dear <|Sian Rodrigues |> , You are Selected ! 
			Dated -> 27-07-2024'''

# 3] Double-Spacing in a String 
detect = input("Enter Any String : ")

if(detect.__contains__("  ")) :
	print("The given string contains doubles spaces")
	detect.replace("  ","**")
else:
	print("The given string does not contains double spaces ")


# 4] String Formatting 

print("Dear Sian, \n \t It's been great meeting you !")


