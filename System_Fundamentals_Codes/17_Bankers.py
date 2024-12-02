def bankers_algorithm(max_req,allocated,available,num_process,num_resources):
    # Here the max_need , allocated will all a 2D list


    need=[[max_req[i][j]-allocated[i][j] for j in range(num_resources)] for i in range(num_process)]
    # Work will signify the number of available resources at any given point 
    # work will be initialised by initil number of available resources

    work=available[:]
    finish=[False]*num_process
    # For keeping track of the safe sequence
    completed_process=[]

    print("Initial Work:", work)
    print("Need Matrix:")
    for n in need:
        print(n)
    
    while len(completed_process)<num_process:
        # returning Whether a safe sequence exists for the given system 
        found =False

        for i in range(num_process):    
        
            # Note that with finish we will be using all() function to return the boolean value for each element in 
            # the list
            # For the Processes who have not yet finished executing
            if not finish[i] and all(work[j] >= need[i][j] for j in range(num_resources)):
                # Releasing all the resources to the process i and adding them to 
                work=[work[j]+allocated[i][j] for j in range(num_resources)]
                finish[i]=True
                found=True
                completed_process.append(f"Process:{i+1}")
                print("Current available resources are : ",work)
                break
        
        # If no sequence can be found till end 
        if not found :
            return False,[]
    return True,completed_process

# Input Example
processes = [0, 1, 2, 3, 4]  # Process IDs
available = [3, 3, 2]  # Available resources
# We can use the loop to input this things from the command line 
max_need = [  # Max resources required for each process
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
allocation = [  # Resources currently allocated to each process
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Check for safe state
is_safe, safe_sequence = bankers_algorithm(max_need, allocation, available, 5,3)
if is_safe:
    print("\nThe system is in a safe state.")
    print("Safe sequence:", safe_sequence)
else:
    print("\nThe system is NOT in a safe state.")



# -------------------------------------------------------
# Understanding all:
# The all() function takes an iterable (e.g., a list, generator, or any object that can be iterated) and returns:

# True if all elements of the iterable are True.
# False if at least one element is False.