# multithreading =  used to perform multiple tasks concurrently (multitasking)
# Good for I/O bound tasks like reading files or fetching data from APIs
# threading.Thread(target=My_functions)


import threading
import time

def goForWalk(name):
    time.sleep(5)
    print(f"Your walking has completed {name}")
def take_out_trash():
    time.sleep(1)
    print('You cleaned the trash well')
def check_msgs(first,last):
    time.sleep(4)
    print(f"Successfully checked your msgs{first} {last}")
# goForWalk()
# take_out_trash()
# check_msgs()
# if we use like this it will execute one after another in order


task1 = threading.Thread(target=goForWalk,args=("Dhanya",))
task1.start()
task2 = threading.Thread(target=take_out_trash)
task2.start()
task3 = threading.Thread(target=check_msgs,args=("Veera", "Lakshmi"))
task3.start()

task1.join()
# these are not mandatory when we want run sequentially but
# if we want to wait other tasks until task1 complete
task2.join()
task3.join()