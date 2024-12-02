import threading

buffer_size=int(input("Enter the size of the buffer : "))
buffer =[]


# Note that here the empty variable checks for empty space in the buffer 
# THIS IS THE MAIN PROCESS OF DECALRING THE SEMAPHORE VARIABLES WITH THE NUMBER OF AVAIABLE INSTANCES
empty=threading.Semaphore(buffer_size)
mutex=threading.Semaphore(1)
full =threading.Semaphore(0)


# note that here in place of semaphore we wll be passing the value of the variable to be decremented
def wait(semaphore):
    semaphore.acquire()

def signal(semaphore):
    semaphore.release()

# ITEM_NUMBER --> to be produced or consumed
def produce_item(item_number):

    wait(mutex)
    wait(empty)

    item=f'Item-Number:{item_number}'
    buffer.append(item)
    print("Producer Produced : ",item)
    # Displaying the current buffer state
    display_buffer_state()

    signal(mutex)
    signal(full)


# IN CASE OF CONSUMER NO INPUT VALUE IS NEEDED AS IT WILL BE CONSUMING THE FIRST PRODUCED ITEM
# WHICH IS AT POSITION 0
def consume_item():
        wait(mutex)
        wait(full)

        buffer.pop(0)
        print("Consumer Consumed an Item")

        # Displaying the buffer state
        display_buffer_state()

        signal(mutex)
        signal(empty)
        
def display_buffer_state():
    #  Printing all the items in the buffer :
     print("Current Buffer state is: ",buffer)


# Random Variable ITEM_NUMBER to be used in order to add items to the buffer initilaised to 1
item_number =1

# Running an Infinite loop for adding and deleting the items in the buffer :
while True :
    sel=input("Enter (p) to produce \n Enter (c) to consume \n Enter (q) to quit :")
    #  for quit break the enitre loop 
    if(sel=='p'):
         
        #  Consume only when there is empty space left in the buffer
        if empty._value>0:
            produce_item(item_number)
            item_number+=1
        else:
             print("Buffer is already Full")      
    elif(sel=='c'):
        if full._value>0:
            #  consume_item does not take any input as a parameter
             consume_item()
    
    elif sel=='q':
         break
    else:
         print("Enter proper input ")
    