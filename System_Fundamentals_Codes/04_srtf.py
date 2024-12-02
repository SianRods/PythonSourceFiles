# AT-[0,1,2,4]
# BT-[5,2,4,1]
# BT[index]=BT[index]-AT[index+1]
# CHECK : if(BT[index+1]<BT[index]) : continue the execution till   next index arrival time .....
# CONDITION FALSE : index++;

# When there is no process in the ready_queue the time_counter should directly jump to the arrival time of the next SORTED process

class Process:
    def __init__(self,name,arrival_time,burst_time):
        self.name=name
        self.arrival_time=arrival_time
        self.burst_time=burst_time
        self.remaining_time=burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def ShortestRemainingTimeFirst(process_queue):
    # Initialising empty ready queue , completed queue and the time counter
    time=0
    ready_queue=[]
    completed_queue=[]
    
    # Sorting the Process Queue Depeding on the arrival time 
    process_queue.sort(key=lambda p:p.arrival_time)

    while process_queue or ready_queue:
        
        # The arrival time should be less than the current_time
        # The Following Loop is used to sequentially add and REMOVE all the process from the process queue 
        # to the ready queue  
        while process_queue and process_queue[0].arrival_time<=time:
            ready_queue.append(process_queue.pop(0))

        # Sorting the processes added in the ready_queue based on their remaining time 
        ready_queue.sort(key=lambda p:p.remaining_time)


        # If there exists process in the ready queue then : 
        if ready_queue:
            # Removing the 'current_process' 
            current_process=ready_queue.pop(0)

            current_process.remaining_time -=1
            time +=1

            if current_process.remaining_time==0:
                current_process.completion_time=time
                current_process.turnaround_time=current_process.completion_time -current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time-current_process.burst_time
                completed_queue.append(current_process)

            else:
                ready_queue.append(current_process)



        # If there are no processes in the ready queue but are in the process_queue
        if not ready_queue and process_queue:
            time=process_queue[0].arrival_time
    for process in completed_queue:
        print(f"{process.name}\t{process.arrival_time}\t{process.burst_time}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}\t\n")

processes = [
    Process('P1', 0, 5),
    Process('P2', 1, 3),
    Process('P3', 2, 4),
    Process('P4', 4, 1)
]

ShortestRemainingTimeFirst(processes)
