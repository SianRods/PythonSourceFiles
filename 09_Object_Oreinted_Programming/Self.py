# The Important thing while creating functions within a Class is that they have to be made 
#  accepting 'self' as an argument 
# for ex)


# Note that self and object s1 are same thing pointing at same memory location 
class Solution: 
	def printName(self) :
		print("This is your name !")

s1 = Solution()
# When i call this function using s1.printName() --> Error Comes up 
# --> : Animal._legs_() takes 0 positional arguments but 1 was given

# s1.printName() --> Solution.printName(s1)
# It Actually Gets Executed like this and hence including the self is important for each and every 
# function wihtin a class

# Note that here the self parameter denotes the 'this' instance of the class 

class Sample:
	a=10
	def __init__(self,a) :
		print(f"The Entered Number is : {a}")

s1= Sample(12)