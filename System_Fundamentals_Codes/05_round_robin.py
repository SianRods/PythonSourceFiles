# AT-[0,1,2,4]
# BT-[5,2,4,1]
# BT[index]=BT[index]-AT[index+1]
# CHECK : if(BT[index+1]<BT[index]) : continue the execution till   next index arrival time .....
# CONDITION FALSE : index++;

class Process:
    def __init__(self,name,arrival_time,burst_time):
        self.name=name
        self.arrival_time=arrival_time
        self.burst_time=burst_time
        self.remaining_time=burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0


def RoundRobin(process_queue,time_quantum):
    # Initialising empty ready queue , completed queue and the time counter
    time=0
    ready_queue=[]
    completed_queue=[]
    

    process_queue.sort(key=lambda p:p.arrival_time)

    while process_queue or ready_queue:

        while process_queue and process_queue[0].arrival_time<=time:
            ready_queue.append(process_queue.pop(0))

        # ready_queue.sort(key=lambda p:p.remaining_time)

        if ready_queue:
            current_process=ready_queue.pop(0)


            #  Implementing the Condition for time Quatum -->  IFF the remaining time is greater than time_quantum
            if(current_process.remaining_time>time_quantum):
                current_process.remaining_time = current_process.remaining_time -time_quantum
                time += time_quantum
          
            #  If the current_process.remaining_time < time_quatum --> just complete that process entirely and add it to the completed queue
            else:
                # Adding the remaining time of the process to the time_counter and ending that given process
                time +=  current_process.remaining_time
                current_process.remaining_time=0
                current_process.completion_time=time
                current_process.turnaround_time=current_process.completion_time -current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time-current_process.burst_time
                completed_queue.append(current_process)

            if current_process.remaining_time:
                ready_queue.append(current_process)

        # When no process is ready (ready_queue is empty), the current time should jump to the next process's arrival time instead of incrementing by 1.
        if not ready_queue and process_queue:
            time=process_queue[0].arrival_time


    for process in completed_queue:
        print(f"{process.name}\t{process.arrival_time}\t{process.burst_time}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}\t\n")

processes = [
    Process('P1', 0, 5),
    Process('P2', 1, 4),
    Process('P3', 2, 2),
    Process('P4', 4, 1)
]

RoundRobin(processes,2)
