def LRU(reference_string,no_frames):
    hit=0
    fault=0
    # Memory will always be of Limited Size 
    memory=[]

    for i in range(len(reference_string)):
        page = reference_string[i]
        
        if page in memory:
            # Page is already in memory (HIT)
            hit += 1

            # THE IS THE MAIN CONCEPT BEHIND LRU 
            # HERE WE WILL MOVING AND APPENDING THE MOST RECENTLY USED PAGE IN THE LAST POSITION WHEN HIT OCCURS
            # SO NOW EVERY TIME WE HAVE FAULT AND AND MEMORY IS FULL THE ELEMENT AT 0TH INDEX IS LEAST USED AND NEEDS
            # TO BE REPLACED
            
            # Move the page to the most recently used position
            memory.remove(page)
            memory.append(page)
        else:
            # Page is not in memory (FAULT)
            fault += 1
            if len(memory) < no_frames:
                # Add page if memory is not full
                memory.append(page)
            else:
                # Memory is full, replace the least recently used page
                memory.pop(0)
                memory.append(page)
    return memory,hit,fault


reference_string=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]


print(f"Final Memory : {LRU(reference_string,3)[0]}\n Number of Hits :{LRU(reference_string,3)[1]}\n Number of Hits :{LRU(reference_string,3)[2]}")

#  NOTE that LRU AND OPTIMAL ARE SIMILAR JUST IN CASE OF LRU WE HAVE TO REFER AND CHECK THE PAST STRING 
# INDICES FROM THE CURRENT STRING INDICES 