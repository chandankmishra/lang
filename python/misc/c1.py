import threading
import time

cv = threading.Condition()
is_even = True


def odd_print():
    """ Thread A will print odd numbers 1,3,...99 """
    global is_even
    for count in range(1, 101, 2):
        cv.acquire()
        while is_even is True:
            cv.wait()
        print ("odd_print ", count)
        is_even = True
        time.sleep(.1)
        cv.notify()
        cv.release()


def even_print():
    global is_even
    for count in range(0, 100, 2):
        cv.acquire()
        while is_even is False:
            cv.wait()
        print ("even_print ", count)
        is_even = False
        time.sleep(.1)
        cv.notify()
        cv.release()


tp = threading.Thread(target=odd_print)
tc = threading.Thread(target=even_print)

tp.start()
tc.start()

tp.join()
tc.join()
