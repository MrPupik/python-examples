from threading import Thread, Lock, current_thread
from time import get_clock_info, sleep
sleep_time = 0.1
num_of_times = 15


# winner = None
lock = Lock()


def protected_print(msg):
    global lock
    lock.acquire()
    print(msg)
    lock.release()


def print_ones():
    global winner, lock
    for i in range(25):
        sleep(sleep_time)
        protected_print(1)
    # lock.acquire()
    # if winner is None:
    #     winner = 1
    # lock.release()


def print_zeroes():
    global winner, lock
    for i in range(num_of_times):
        sleep(sleep_time)
        protected_print(0)
    # lock.acquire()
    # if winner is None:
    #     winner = 0
    # lock.release()


# phase 1
t1 = Thread(target=print_ones)


t1.start()
print_zeroes()
# t1.join()
print("Done !")


# phase 2

# t1 = Thread(target=print_ones)
# t2 = Thread(target=print_zeroes)
# t1.start()
# t2.start()

# t1.join()
# t2.join()

# sleep(0.1)
# print("done ! winner is: "+str(winner))
