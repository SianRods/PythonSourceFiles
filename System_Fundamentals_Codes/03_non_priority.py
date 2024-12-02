# Here we consider the priority of the given processes if they arrive at the same Time 
# Priority queue 
# Sorting Indexes Based on the Priority


# --------------------------------------------------------------------------------------------------------
size=int(input("Enter the Number of Processes: "))
arrival_time=[x for x in range(0,size)]
burst_time=[x for x in range(0,size)]
priority_list=[x for x in range(0,size)]


for i in range(size):
    arrival_time[i]=int(input(f"Enter the Arrival time for Process P{i+1}:  "))

for i in range(size):
    burst_time[i]=int(input(f"Enter the Burst time for Process P{i+1}:  "))

for i in range(size):
    priority_list[i]=int(input(f"Enter the Priority Order for Process P{i+1}:  "))


def NonPriority(arrival_time,burst_time,size,priority_list):
    completion_time=[x for x in range(0,size)]
    turn_around_time=[x for x in range(0,size)]
    waiting_time=[x for x in range(0,size)]
    # We have to keep updating the list after every successful execution
    remaining_list=[x for x in range(size)]

    time_counter=0

    while remaining_list:
        # Maintining a ready queue and adding process dynamically to the ready queue : 
        ready_queue=[i for i in remaining_list if arrival_time[i]<=time_counter]

        # If there are processes waiting in the ready queue then sort
        if ready_queue:
            # Getting the index with minimum burst time : 
            priority_index= min(ready_queue,key=lambda i: priority_list[i])
            time_counter+=burst_time[priority_index]
            completion_time[priority_index]=time_counter
            turn_around_time[priority_index] = completion_time[priority_index]-arrival_time[priority_index]
            waiting_time[priority_index]=turn_around_time[priority_index]-burst_time[priority_index]
            remaining_list.remove(priority_index)
        
        else:
            # If no process is ready, increment time to the next arrival
            # Sequentially increasing the time_counter by one 
            time_counter +=1





    return completion_time,turn_around_time,waiting_time


print(NonPriority(arrival_time,burst_time,size,priority_list))




