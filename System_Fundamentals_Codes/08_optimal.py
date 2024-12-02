def OPTIMAL(reference_string,no_frames):
    hit=0
    fault=0
    # Memory will always be of Limited Size 
    memory=[]

    for i in range(len(reference_string)):
        page = reference_string[i]
        
        if page in memory:
            # Page is already in memory (HIT)
            hit += 1
        else:
            # Page is not in memory (FAULT)
            fault += 1
            if len(memory) < no_frames:
                # Add page if memory is not full
                memory.append(page)
            else:
                # Memory is full, find the optimal page to replace
                future_pages = reference_string[i + 1:]
                indices = []
                
                for page_in_memory in memory:
                    if page_in_memory in future_pages:
                        indices.append(future_pages.index(page_in_memory))
                    else:
                        indices.append(float('inf'))  # Page not needed in the future
                
                # Find the page with the maximum index (farthest in the future or not used)
                page_to_replace_index = indices.index(max(indices))
                memory[page_to_replace_index] = page

                
    return memory,hit,fault


reference_string=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]


print(f"Final Memory : {OPTIMAL(reference_string,3)[0]}\n Number of Hits :{OPTIMAL(reference_string,3)[1]}\n Number of Hits :{OPTIMAL(reference_string,3)[2]}")