# -------------------------------------------------------------------------------------------------------------------------
# Implementing Preemptive-Priority Scheduling Algorithm 
#  Steps : --> 
# 1. Run the process for spcific time quantum or say (1 ms )
# 2.check if processes of higher priority have arrived 
# 3. run the process with higher priority 
# 4. Continue Repeating above points 
# ---------------------------------------------------------------------------------------------------------------------------

class Process:
    def __init__(self,name,arrival_time,burst_time,priority):
        self.name=name
        self.priority=priority
        self.arrival_time=arrival_time
        self.burst_time=burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.remaining_time=burst_time
        self.waiting_time = 0

def PremtivePriority(process_queue):
    # Initialising empty ready queue , completed queue and the time counter
    time=0
    ready_queue=[]
    completed_queue=[]
    

    process_queue.sort(key=lambda p:p.arrival_time)

    while process_queue or ready_queue:
        
        # The arrival time should be less than the current_time
        while process_queue and process_queue[0].arrival_time<=time:
            ready_queue.append(process_queue.pop(0))

        ready_queue.sort(key=lambda p:p.priority)

        if ready_queue:
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
    Process('P1', 0, 5,40),
    Process('P2', 1, 4,30),
    Process('P3', 2, 2,20),
    Process('P4', 4, 1,10)
]

PremtivePriority(processes)

# Check the priority order before --> Higher the number higher the priority
# Or lower the number 
