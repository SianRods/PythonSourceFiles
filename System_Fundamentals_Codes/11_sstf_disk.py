# reference _string =[0,16,24,43,50,82,140,170,190,199]
# current_postition =50
# track_movement =0 --> incremented on each step 
# change of track_movement on every loop 

# We always have to consider the absolute value of the difference 
import numpy as np 

def SSTF_DISK(current_track,reference_string):
    track_movement=0
    for i in range(len(reference_string)):
        temp_list=np.array(reference_string)-current_track
        temp_list=list(temp_list)
        track_movement += abs(current_track-reference_string[temp_list.index(min(temp_list))])
        # Pop the index which has been served if the current_read_write_head exists in the list 
        if current_track in reference_string:
            reference_string.pop(reference_string.index(current_track))
        current_track=reference_string[temp_list.index(min(temp_list))]
        reference_string.pop(temp_list.index(min(temp_list)))
    return track_movement
    
reference_string=[82,170,43,140,24,16,190]
print(f"The total track movement if : {SSTF_DISK(50,reference_string)}")



# Approach -> temp=reference_list-current_head 
# min(temp).index --> 
# shift the current_head to the minimum index_value and repeat