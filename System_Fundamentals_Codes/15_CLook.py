
import matplotlib.pyplot as plt 

def cscan(current_head,reference_string,total_tracks):
    first_track=0
    last_track=total_tracks-1

    # Sorting the reference_list : 
    reference_string=sorted(reference_string)
    # breaking up the list using the    
    upper_bound=[i for i in reference_string if i>=current_head]
    lower_bound=[i for i in reference_string if i<current_head]

    track_movement=0
    header_list=[]
    
    # Loop till len(upper_bound)+1 to consider the last track within the loop itself
    # or assign the last track after this loop is completed
    for i in range(len(upper_bound)):
        header_list.append(current_head)
        track_movement += abs(current_head-upper_bound[i])
        current_head=upper_bound[i]



    
    # Sort the Lower list in the descending order :
    track_movement+=upper_bound[len(upper_bound)-1]-lower_bound[0]

    current_head=lower_bound[0]

    lower_bound.sort()
    for i in range(len(lower_bound)):
        header_list.append(current_head)
        track_movement += abs(current_head-lower_bound[i])
        current_head=lower_bound[i]


    
    return track_movement,header_list

reference_list=[16,24,43,50,82,140,170,190]
total_tracks=200
movement,header=cscan(50,reference_list,total_tracks)
print("Total Track Movement is : ",movement)

# Drawing the head movement v/s reference list 
plt.title("Head Movement Tracker")
plt.legend()
plt.xlabel("Reference List")
plt.ylabel("Increasing header Position")
plt.plot(header,reference_list)
plt.show()