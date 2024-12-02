# Here the criteria is the Arrival Time 
# AT-[0,1,5,6]
# BT-[2,2,3,4]
# Creating Empty Lists Consisting of Completion Time , Turn around Time , Waiting Time 
# Completion time = instance at which the program get's completed = current_counter_time
# TAT = Completion Time[i] - Arrival Time[i]
# Waiting Time = TAT[i] - BurstTime [i] 
# A variable must be there to keep the track of the time from start 
# Number of Processes = 4
# arrival_time[4] ; burst_time[4]
# Finding the minimum arrival time and it's corresponding index
# Indexing for Minimum Value list.index(value) --> returns the index of the first value occurence
# req_index=index
# current_counter_time=0
# We have to also include the Edge Case When CPU will be ideal and add that time to the time_counter 
# ----------------------------------------------------------------------------------------------------------------

size=int(input("Enter the Number of Processes: "))
arrival_time=[x for x in range(0,size)]
burst_time=[x for x in range(0,size)]
for i in range(size):
    arrival_time[i]=int(input(f"Enter the Arrival time for Process P{i+1}"))

for i in range(size):
    burst_time[i]=int(input(f"Enter the Burst time for Process P{i+1}"))


def FirstComeFirstServe(arrival_time,burst_time,size):
    completion_time=[x for x in range(0,size)]
    turn_around_time=[x for x in range(0,size)]
    waiting_time=[x for x in range(0,size)]

    # Initialising the Time Counter 
    time_counter=0

    for i in range(size):
        # Picking the index with lowest arrival time : 
        index= arrival_time.index(min(arrival_time))

        # Adjusting the Ideal Time of the CPU with the time_counter 
        if(arrival_time[index]>time_counter):
            time_counter+=arrival_time[index]-time_counter
            
        time_counter+=burst_time[index]
        completion_time[index]=time_counter
        turn_around_time[index]=completion_time[index]-arrival_time[index]
        waiting_time[index]=turn_around_time[index]-burst_time[index]
        arrival_time[index]=999999

    return completion_time,turn_around_time,waiting_time


print(FirstComeFirstServe(arrival_time,burst_time,size))



# -----------------------------------------------------------------------------------------------------
# FCFS can also be implemented as follows :
# Method 2 : 
# here in this case i will sort the indexes based on the arrival time 
# sorted_indices= sorted(range(size),key=lambda i : arrival_time[i])



