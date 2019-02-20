FREE = 0
BUSY = 1
def spinlock_init(lock):
    lock = FREE


# test and set spinlock 
def spinlock_lock1(lock):
    while test_and_set(lock) == BUSY:
        pass

# test and test and set spinlock 
def spinlock_lock1(lock):
    while lock == BUSY or test_and_set(lock) == BUSY:
        pass

# test and test and set spinlock with delay 
def spinlock_lock1(lock):
    while lock == BUSY or test_and_set(lock) == BUSY:
        while lock == BUSY:
            delay()

def spinlock_unlock(lock):
    lock = FREE    


####### Queue based spin lock ####
init:
    flags[0] = has-lock
    flags[1..p-1] = must-wait
    queuelast = 0 # global variable
    
lock:
    myplace = read_and_increment_atomic(queuelast)
    # spin
    while (flags[myplace % p] == must-wait):
        pass
    #
    # Critical section
    #
    flags[myplace % p] = must-wait
 
unlock:
    flags[(myplace + 1) % p] = has-lock
