def FIFO(reference_string,no_frames):
    hit=0
    fault=0
    # Memory will always be of Limited Size 
    memory=[]

    for i in range(len(reference_string)):
        if(reference_string[i] in memory):
            hit+=1
        else:
        #   IF THE MEMORY IF FULL THEN --> 
            if(len(memory)==no_frames):
                fault+=1
                memory.pop(0)
                # Appending at the end of the list so the first-in-first-out condition remains
                memory.append(reference_string[i])
        # IF THE MEMORY IS NOT FULL THEN : -->
            else:
                # If no page is initially added to the memoryy
                fault+=1
                memory.append(reference_string[i])
    return memory,hit,fault


reference_string=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]


print(f"Final Memory : {FIFO(reference_string,3)[0]}\n Number of Hits :{FIFO(reference_string,3)[1]}\n Number of Hits :{FIFO(reference_string,3)[2]}")