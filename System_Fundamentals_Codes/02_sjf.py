# Everything is same as compared to first come first serve 
# For Same Arrival Time --> lowest burst time factor is considered
# In other words we can also have the sorted indices using lambda functions which must be executed 
# at -[1,2,1,4] ; bt- [3,4,2,4]
# Sorts the indices according to their burst time 
# sorted(range()size,key =lambda :i burst_time[i]))

# ------------------------------------------------------------------------------------------------------

size=int(input("Enter the Number of Processes: "))
arrival_time=[x for x in range(0,size)]
burst_time=[x for x in range(0,size)]
for i in range(size):
    arrival_time[i]=int(input(f"Enter the Arrival time for Process P{i+1} : "))

for i in range(size):
    burst_time[i]=int(input(f"Enter the Burst time for Process P{i+1} : "))


def ShortestJobFirst(arrival_time,burst_time,size):
    completion_time=[x for x in range(0,size)]
    turn_around_time=[x for x in range(0,size)]
    waiting_time=[x for x in range(0,size)]
    remaining_processes=[x for x in range(size)]

    # Initialising the Time Counter 
    time_counter=0
    while remaining_processes:
        # Filter processes that have arrived and are yet to be executed
        # Adding the processes to the ready queue
        ready_queue = [i for i in remaining_processes if arrival_time[i] <= time_counter]
        
        if ready_queue:
            # Select the process with the shortest burst time from the ready queue
            # Selecting the minimum index value 
            shortest_job = min(ready_queue, key=lambda i: burst_time[i])
            remaining_processes.remove(shortest_job)
            
            # Update time counter and calculate completion time
            time_counter += burst_time[shortest_job]
            completion_time[shortest_job] = time_counter
            turn_around_time[shortest_job]=completion_time[shortest_job]-arrival_time[shortest_job]
            waiting_time[shortest_job]=turn_around_time[shortest_job]-burst_time[shortest_job]
        else:
            # If no process is ready, increment time to the next arrival
            # Sequentially increasing the time_counter by one 
            time_counter += 1
        

    return completion_time,turn_around_time,waiting_time


print(ShortestJobFirst(arrival_time,burst_time,size))

# -----------------------------------------------------------------------------------------------------