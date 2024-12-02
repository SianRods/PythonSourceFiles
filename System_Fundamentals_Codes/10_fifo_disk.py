# reference _string =[0,16,24,43,50,82,140,170,190,199]
# current_postition =50
# track_movement =0 --> incremented on each step 
# change of track_movement on every loop 

# We always have to consider the absolute value of the difference 


def FIFO_DISK(current_track,reference_string):
    track_movement=0
    for i in range(len(reference_string)):
        track_movement += abs(current_track-reference_string[i])
        current_track=reference_string[i]

    return track_movement
    
reference_string=[82,170,43,140,24,16,190]
print(f"The total track movement if : {FIFO_DISK(50,reference_string)}")


#  we should also include the total tracks in the for scan and look algorithms