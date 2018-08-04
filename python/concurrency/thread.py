import threading
import time
import random

def executeThread(i):
    print(f"Thread {i} started\n")
    sleepTime = random.randint(1,10)
    time.sleep(sleepTime)
    print(f"Thread {i} finished executing\n")

thread = {}

#start 10 threads
for i in range(10):
    thread[i] = threading.Thread(target=executeThread, args=(i,))
    thread[i].start()

    '''
    print("Active Threads:")
    for t in threading.enumerate():
        print (t)
    '''
# wait for all 10 threads to finish
for i in range(10):
    thread[i].join()

# end of main thread 
print ("End of main thread!!!")
    
