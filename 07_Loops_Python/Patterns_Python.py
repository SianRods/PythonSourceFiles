
rows =int(input("Enter the number of rows you want to print : "))

for i in range(0,rows):
    for j in range(0,i):
        print("*",end="")
    print("\n")