# Problem No 1--> Dictionary 
Translate={
	"Mokka":'Chance',
	"Nokri":"Job",
	"Naam":"Name ",
	"Vada-Pav":"BestfOOD"
}

print(Translate.keys())
print(Translate[input("Enter the Word You Want to Translate : ")])

# Problem No.2 
# using an empty set 
nums = set()
print("Enter Any Eight Numbers : ")
nums.add(int(input("Enter the First Number : ")))
nums.add(int(input("Enter the Second Number : ")))
nums.add(int(input("Enter the Third Number : ")))
nums.add(int(input("Enter the Fourth Number : ")))
nums.add(int(input("Enter the Fifth Number : ")))
nums.add(int(input("Enter the Sixth Number : ")))
nums.add(int(input("Enter the Sventh Number : ")))
nums.add(int(input("Enter the Eight Number : ")))

print(nums)

# Problem No3 

s=set()
s.add(8)
s.add("8")
print(s)

# Problem No 4
se= set() 
se.add(20) 
se.add(20.0) 
se.add('20')
# Length of the Se -->Will be 2 as both the type 20 and 20.0 are identified as same 

# Problem No 7 --> Changing Value inside a list contained in S ()

s = {8, 7, 12, "Harry", [1,2]}
# Nope cause the list is  contained within the set and the containes of the sets can't be  changed  





