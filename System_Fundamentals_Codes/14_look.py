
def look(current_head,reference_string,total_tracks):
    first_track=0
    last_track=total_tracks-1

    # Sorting the reference_list : 
    reference_string=sorted(reference_string)
    # breaking up the list using the    
    upper_bound=[i for i in reference_string if i>=current_head]
    lower_bound=[i for i in reference_string if i<current_head]

    track_movement=0
    
    # Loop till len(upper_bound)+1 to consider the last track within the loop itself
    # or assign the last track after this loop is completed
    for i in range(len(upper_bound)):
        track_movement += abs(current_head-upper_bound[i])
        current_head=upper_bound[i]



    lower_bound.sort(reverse=True)
   
    for i in range(len(lower_bound)):
        track_movement += abs(current_head-lower_bound[i])
        current_head=lower_bound[i]


    
    return track_movement

reference_list=[16,24,43,50,82,140,170,190]
total_tracks=200
print("Total Track Movement is : ",look1(50,reference_list,total_tracks))